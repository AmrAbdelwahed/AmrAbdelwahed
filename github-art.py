import os
import subprocess
from datetime import datetime, timedelta
import random

# Starting date - setting to about 6 months ago for optimal current visibility
start_date = datetime(2024, 5, 1)

# Design pattern for "A.A :)" where:
# Numbers represent commit counts (0 = no commits, 1-5 = number of commits for height variation)
# Each sublist represents a column (Sunday to Saturday)
design = [
    # First A (taller in the middle)
    [0, 3, 4, 3, 0, 0, 0],  # Top of A
    [0, 2, 0, 2, 0, 0, 0],  # Middle sides of A
    [0, 4, 5, 4, 0, 0, 0],  # Middle cross of A (tallest)
    [0, 2, 0, 2, 0, 0, 0],  # Bottom of A
    # Period (small but visible)
    [0, 0, 0, 0, 0, 0, 0],  # Space
    [0, 0, 2, 0, 0, 0, 0],  # Period
    # Second A (slightly different heights for variety)
    [0, 3, 4, 3, 0, 0, 0],
    [0, 2, 0, 2, 0, 0, 0],
    [0, 4, 5, 4, 0, 0, 0],
    [0, 2, 0, 2, 0, 0, 0],
    # Space before smiley
    [0, 0, 0, 0, 0, 0, 0],
    # Smiley face (varying heights for 3D effect)
    [0, 3, 0, 0, 0, 3, 0],  # Eyes (medium height)
    [0, 0, 0, 0, 0, 0, 0],  # Space
    [2, 0, 0, 0, 0, 0, 2],  # Sides of smile
    [0, 3, 4, 5, 4, 3, 0],  # Bottom of smile (varying heights)
]

def create_git_art(repo_path):
    """
    Creates git commits according to the design pattern with height variation
    """
    if not os.path.exists(repo_path):
        raise ValueError(f"Repository path {repo_path} does not exist!")
    
    os.chdir(repo_path)
    
    # Ensure we're on the main branch
    subprocess.run(["git", "checkout", "main"], capture_output=True)
    
    commit_count = 0
    
    # Create commits according to the pattern
    for col, row_values in enumerate(design):
        for row, commit_num in enumerate(row_values):
            if commit_num > 0:
                # Calculate the date for this position
                date = start_date + timedelta(days=(col * 7) + row)
                
                # Create multiple commits for height variation
                for i in range(commit_num):
                    # Add some time variation within the day
                    commit_time = date + timedelta(hours=i*2)
                    
                    # Create commit with a unique message
                    subprocess.run([
                        "git", 
                        "commit", 
                        "--allow-empty", 
                        "-m", f"Contribution art ({commit_count}): {commit_time.strftime('%Y-%m-%d %H:%M')}",
                        "--date", commit_time.strftime("%Y-%m-%dT%H:%M:%S")
                    ])
                    commit_count += 1
    
    # Add some random noise commits for natural looking pattern
    add_noise_commits(start_date, 20)  # Add 20 random commits
    
    # Push changes to remote repository
    print(f"Created {commit_count} commits. Pushing to remote...")
    subprocess.run(["git", "push", "origin", "main"])

def add_noise_commits(start_date, num_noise_commits):
    """
    Adds some random commits to make the pattern look more natural
    """
    for _ in range(num_noise_commits):
        # Random date within the year
        random_days = random.randint(0, 365)
        noise_date = start_date + timedelta(days=random_days)
        
        subprocess.run([
            "git",
            "commit",
            "--allow-empty",
            "-m", f"Additional contribution: {noise_date.strftime('%Y-%m-%d')}",
            "--date", noise_date.strftime("%Y-%m-%dT%H:%M:%S")
        ])

def verify_git_config():
    """
    Verifies git configuration is set up correctly
    """
    try:
        # Check if git user name and email are configured
        name = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True)
        email = subprocess.run(["git", "config", "user.email"], capture_output=True, text=True)
        
        if not name.stdout.strip() or not email.stdout.strip():
            print("Warning: Git user name or email not configured!")
            return False
        return True
    except subprocess.CalledProcessError:
        print("Error: Git is not properly installed or configured!")
        return False

if __name__ == "__main__":
    # Replace with your repository path
    repo_path = "."  # Option 1: Current directory
    
    if verify_git_config():
        try:
            create_git_art(repo_path)
            print("Successfully created and pushed contribution art!")
            print("Please check your GitHub profile in a few minutes.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    else:
        print("Please configure git before running this script.")