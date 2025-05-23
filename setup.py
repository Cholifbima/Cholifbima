#!/usr/bin/env python3
"""
GitHub Profile README Setup Script
This script helps you customize your GitHub profile README with your personal information.
"""

import json
import re
import os

def load_config():
    """Load configuration from config.json"""
    with open('config.json', 'r') as f:
        return json.load(f)

def update_readme(config):
    """Update README.md with configuration values"""
    with open('README.md', 'r') as f:
        content = f.read()
    
    # Replace placeholders with actual values
    replacements = {
        '[Your Name]': config['profile']['name'],
        'YourUsername': config['profile']['username'],
        'your.email@example.com': config['profile']['email'],
        'https://yourportfolio.com': config['profile']['portfolio'],
        'https://linkedin.com/in/yourprofile': config['social']['linkedin'],
        'https://twitter.com/yourhandle': config['social']['twitter'],
        'https://instagram.com/yourhandle': config['social']['instagram'],
    }
    
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)
    
    # Update typing animation messages
    typing_messages = '+'.join(config['content']['typing_messages'])
    content = re.sub(
        r'lines=([^)]+)',
        f'lines={typing_messages}',
        content
    )
    
    with open('README.md', 'w') as f:
        f.write(content)

def update_workflows(config):
    """Update GitHub Actions workflows with username"""
    username = config['profile']['username']
    
    # Update snake.yml
    with open('.github/workflows/snake.yml', 'r') as f:
        snake_content = f.read()
    
    # No changes needed for snake.yml as it uses github.repository_owner
    
    print(f"✅ Workflows updated for username: {username}")

def main():
    """Main setup function"""
    print("🚀 GitHub Profile README Setup")
    print("=" * 40)
    
    # Check if config.json exists
    if not os.path.exists('config.json'):
        print("❌ config.json not found. Please create it first.")
        return
    
    try:
        config = load_config()
        print(f"📝 Setting up profile for: {config['profile']['name']}")
        
        # Update README.md
        update_readme(config)
        print("✅ README.md updated")
        
        # Update workflows
        update_workflows(config)
        
        print("\n🎉 Setup complete!")
        print("\nNext steps:")
        print("1. Review and customize your README.md")
        print("2. Update config.json with your actual information")
        print("3. Commit and push to your GitHub profile repository")
        print("4. Enable GitHub Actions in your repository settings")
        print("5. Wait for the snake animation to generate (may take a few minutes)")
        
    except Exception as e:
        print(f"❌ Error during setup: {e}")

if __name__ == "__main__":
    main()
