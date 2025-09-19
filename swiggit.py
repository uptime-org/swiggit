#!/usr/bin/env python3
"""
🍀 SWIGGIT - Multi-Organization Git CLI Tool 💰
Irish Gold Theme with Rainbow Animations
"""

import os
import sys
import subprocess
import json
import time
import requests
from pathlib import Path
import configparser
from typing import Tuple, Optional, Dict, Any

# Irish Gold Rainbow Theme Colors 🌈💰🍀
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    MAGENTA = '\033[0;95m'
    ORANGE = '\033[0;33m'
    PINK = '\033[0;91m'
    LIME = '\033[0;92m'
    SKY = '\033[0;96m'
    LAVENDER = '\033[0;94m'
    GOLD = '\033[1;93m'
    EMERALD = '\033[1;92m'
    # Custom backgrounds
    BG_GOLD = '\033[48;5;220m'
    BG_GREEN = '\033[48;5;34m'
    BG_RAINBOW = '\033[48;5;57m'
    NC = '\033[0m'  # No Color

def pot_of_gold_animation():
    """Animation for pot of gold success"""
    print(f"{Colors.BG_GOLD}{Colors.GREEN}🌈 Validating...{Colors.NC}", end="", flush=True)
    for i in range(3):
        print(f"{Colors.GOLD}.", end="", flush=True)
        time.sleep(0.3)
    print(f" {Colors.BG_GOLD}{Colors.GREEN}💰 Success! {Colors.NC}")

def print_success(msg):
    pot_of_gold_animation()
    print(f"{Colors.BG_GOLD}{Colors.GREEN}🍀 {Colors.GOLD}💰 {msg}{Colors.NC}")

def print_error(msg):
    print(f"{Colors.BG_RAINBOW}{Colors.RED}☁️ {Colors.PINK}⚡ {msg}{Colors.NC}")

def print_info(msg):
    print(f"{Colors.SKY}☁️ {Colors.CYAN}🌈 {msg}{Colors.NC}")

def print_warning(msg):
    print(f"{Colors.BG_GREEN}{Colors.ORANGE}⚡ {Colors.YELLOW}🍀 {msg}{Colors.NC}")

def print_header():
    print(f"{Colors.BG_GREEN}{Colors.GOLD}╔══════════════════════════════════════════╗{Colors.NC}")
    print(f"{Colors.BG_GREEN}{Colors.GOLD}║{Colors.NC} 🍀 {Colors.RED}S{Colors.ORANGE}W{Colors.YELLOW}I{Colors.GOLD}G{Colors.EMERALD}G{Colors.SKY}I{Colors.BLUE}T{Colors.LAVENDER} 🌈💰 {Colors.CYAN}Multi-Org Git CLI{Colors.NC} 🍀 {Colors.BG_GREEN}{Colors.GOLD}║{Colors.NC}")
    print(f"{Colors.BG_GREEN}{Colors.GOLD}╚══════════════════════════════════════════╝{Colors.NC}")

# Git Command Abstraction with Identity Management 🍀💰
class GitCommand:
    """Abstraction for all git commands with consistent identity injection"""
    
    def __init__(self, org_config: Dict[str, Any]):
        self.org_config = org_config
        self.ssh_key = org_config.get('ssh_key_path', '')
        self.git_user = org_config.get('git_user_name', '')
        self.git_email = org_config.get('git_user_email', '')
        
    def get_env(self) -> Dict[str, str]:
        """Get environment with SSH configuration"""
        env = os.environ.copy()
        env["GIT_SSH_COMMAND"] = f"ssh -i {self.ssh_key} -o IdentitiesOnly=yes"
        return env
    
    def build_command(self, git_args: str) -> str:
        """Build complete git command with identity parameters"""
        return f'git -c user.name="{self.git_user}" -c user.email="{self.git_email}" {git_args}'
    
    def execute(self, git_args: str, capture_output: bool = True) -> Tuple[bool, str, str]:
        """Execute git command with identity injection"""
        cmd = self.build_command(git_args)
        env = self.get_env()
        
        print_info(f"🔧 Git: {git_args}")
        
        try:
            if capture_output:
                result = subprocess.run(cmd, shell=True, env=env, 
                                      capture_output=True, text=True)
                return result.returncode == 0, result.stdout, result.stderr
            else:
                result = subprocess.run(cmd, shell=True, env=env)
                return result.returncode == 0, "", ""
        except Exception as e:
            return False, "", str(e)
    
    def init(self) -> Tuple[bool, str, str]:
        """Initialize git repository with identity"""
        return self.execute("init")
    
    def add(self, files: str = ".") -> Tuple[bool, str, str]:
        """Add files to staging"""
        return self.execute(f"add {files}")
    
    def commit(self, message: str) -> Tuple[bool, str, str]:
        """Commit with message"""
        return self.execute(f'commit -m "{message}"')
    
    def remote_add(self, name: str, url: str) -> Tuple[bool, str, str]:
        """Add remote repository"""
        return self.execute(f"remote add {name} {url}")
    
    def remote_remove(self, name: str) -> Tuple[bool, str, str]:
        """Remove remote repository"""
        return self.execute(f"remote remove {name}")
    
    def push(self, remote: str = "origin", branch: str = "main", set_upstream: bool = False) -> Tuple[bool, str, str]:
        """Push to remote repository"""
        args = f"push {'-u ' if set_upstream else ''}{remote} {branch}"
        return self.execute(args)
    
    def config_set(self, key: str, value: str) -> Tuple[bool, str, str]:
        """Set git config value"""
        return self.execute(f'config {key} "{value}"')
    
    def status(self) -> Tuple[bool, str, str]:
        """Get git status"""
        return self.execute("status --porcelain")
    
    def get_identity_summary(self) -> str:
        """Get formatted identity summary for display"""
        return f"👤 {self.git_user} <{self.git_email}> 🔑 {self.ssh_key}"

class SwiggitConfig:
    def __init__(self):
        self.config = {}
        self.load_config()
    
    def load_config(self):
        """Load configuration from JSON file"""
        # Try to find the config file in multiple locations
        possible_paths = [
            Path(".swiggit.json"),
            Path.home() / ".swiggit.json",
            Path(".ssh/.swiggit.json")
        ]
        
        config_file = None
        for path in possible_paths:
            if path.exists():
                config_file = path
                break
                
        if not config_file:
            print_error(f"SWIGGIT JSON config file not found. Tried: {[str(p) for p in possible_paths]}")
            sys.exit(1)
            
        print_info(f"Loading config from: {config_file}")
        
        # Load JSON configuration
        try:
            with open(config_file, 'r') as f:
                self.config = json.load(f)
            print_info("✅ JSON config loaded successfully")
        except json.JSONDecodeError as e:
            print_error(f"Failed to parse JSON config: {e}")
            sys.exit(1)
        except Exception as e:
            print_error(f"Failed to load config: {e}")
            sys.exit(1)
    
    def get(self, org, setting):
        """Get setting for specific organization"""
        # First try organization-specific settings
        if org in self.config.get('organizations', {}):
            org_config = self.config['organizations'][org]
            if setting in org_config:
                return org_config[setting]
        
        # Fall back to global settings based on setting name
        if setting == 'ssh_key_path':
            key_path = self.config.get('ssh', {}).get('key_path', '')
            # Only expand ~ for home directory, leave relative paths as-is
            return os.path.expanduser(key_path) if key_path.startswith('~') else key_path
        elif setting == 'git_user_name':
            return self.config.get('git', {}).get('user_name', '')
        elif setting == 'git_user_email':
            return self.config.get('git', {}).get('user_email', '')
        elif setting == 'ssh_options':
            return self.config.get('ssh', {}).get('options', '')
        
        return ""

# Base Repository Creator
class RepositoryCreator:
    def __init__(self, config, org_config):
        self.config = config
        self.org_config = org_config
        self.git = GitCommand(org_config)
    
    def _execute_api_call(self, api_url, payload):
        """Execute the GitHub API call to create repository"""
        temp_dir = "/tmp/swiggit_temp_auth"
        os.makedirs(temp_dir, exist_ok=True)
        
        try:
            # Setup temp git context using GitCommand
            temp_git = GitCommand(self.org_config)
            
            # Change to temp directory and initialize
            original_dir = os.getcwd()
            os.chdir(temp_dir)
            
            success, stdout, stderr = temp_git.init()
            if not success:
                raise Exception(f"Git init failed: {stderr}")
            
            # Set user config in temp repo
            temp_git.config_set('user.name', self.git.git_user)
            temp_git.config_set('user.email', self.git.git_email)
            
            # Execute API call with configured GitHub token
            env = temp_git.get_env()
            github_token = self.org_config.get('github_token', '')
            
            if not github_token or github_token == 'REPLACE_WITH_YOUR_PERSONAL_ACCESS_TOKEN':
                print_error("No GitHub token configured! Please add your personal access token to .swiggit.json")
                print_info("1. Go to https://github.com/settings/tokens")
                print_info("2. Generate a new token with 'repo' scope")
                print_info("3. Replace 'REPLACE_WITH_YOUR_PERSONAL_ACCESS_TOKEN' in .swiggit.json")
                return False, "No GitHub token configured"
            
            print_info(f"🔐 Using configured GitHub token for {self.git.git_user}...")
            
            curl_cmd = f'''
            curl -s -X POST \
                -H "Accept: application/vnd.github.v3+json" \
                -H "User-Agent: swiggit-cli-python" \
                -H "Authorization: token {github_token}" \
                -d '{json.dumps(payload)}' \
                "{api_url}"
            '''
            
            result = subprocess.run(curl_cmd, shell=True, env=env, capture_output=True, text=True)
            
            if result.returncode == 0:
                try:
                    response = json.loads(result.stdout)
                    if 'html_url' in response:
                        return True, response['html_url']
                    else:
                        return False, result.stdout
                except json.JSONDecodeError:
                    return False, result.stdout
            else:
                return False, result.stderr
        except Exception as e:
            return False, str(e)
        finally:
            os.chdir(original_dir) if 'original_dir' in locals() else None
            subprocess.run(f"rm -rf {temp_dir}", shell=True)
    
    def create_repository(self, repo_name, description="", private=True):
        """Abstract method to create repository - must be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement create_repository")

# Personal Account Repository Creator
class PersonalRepositoryCreator(RepositoryCreator):
    def create_repository(self, repo_name, description="", private=True):
        """Create repository in personal GitHub account"""
        print_info("Creating personal repository via GitHub API...")
        
        payload = {
            "name": repo_name,
            "private": private
        }
        
        if description:
            payload["description"] = description
        
        # Personal repo API endpoint
        api_url = "https://api.github.com/user/repos"
        
        return self._execute_api_call(api_url, payload)

# Organization Repository Creator
class OrganizationRepositoryCreator(RepositoryCreator):
    def __init__(self, config, org_config, org_name):
        super().__init__(config, org_config)
        self.org_name = org_name
    
    def create_repository(self, repo_name, description="", private=True):
        """Create repository in GitHub organization"""
        print_info(f"Creating repository in organization '{self.org_name}' via GitHub API...")
        
        payload = {
            "name": repo_name,
            "private": private
        }
        
        if description:
            payload["description"] = description
        
        # Organization repo API endpoint
        api_url = f"https://api.github.com/orgs/{self.org_name}/repos"
        
        return self._execute_api_call(api_url, payload)


class SwiggitCLI:
    def __init__(self):
        self.config = SwiggitConfig()
        
    def get_git_command(self, org_key: str) -> GitCommand:
        """Get GitCommand instance for specific organization"""
        org_config = self.config.config.get('organizations', {}).get(org_key, {})
        # Fallback to global config if org-specific config is missing
        if not org_config.get('ssh_key_path'):
            org_config['ssh_key_path'] = self.config.get(org_key, "ssh_key_path")
        if not org_config.get('git_user_name'):
            org_config['git_user_name'] = self.config.get(org_key, "git_user_name")
        if not org_config.get('git_user_email'):
            org_config['git_user_email'] = self.config.get(org_key, "git_user_email")
        
        return GitCommand(org_config)
    
    def create_repository_creator(self, org_key):
        """Factory method to create appropriate repository creator"""
        org_config = self.config.config.get('organizations', {}).get(org_key, {})
        
        # Determine if this is a personal account or organization
        if org_key == 'personal' or org_config.get('name') == 'personal':
            return PersonalRepositoryCreator(self.config, org_config)
        else:
            # For organizations, use the org_key as the organization name
            org_name = org_config.get('github_org_name', org_key)
            return OrganizationRepositoryCreator(self.config, org_config, org_name)
    
    def create_repository(self):
        """Main repository creation flow"""
        print_header()
        print("🆕 Creating New Repository")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        # Use default org from config
        org_key = self.config.config.get('default', {}).get('org', 'personal')
        org_config = self.config.config.get('organizations', {}).get(org_key, {})
        
        # Get GitCommand instance for this organization
        git = self.get_git_command(org_key)
        
        org_name = org_config.get('name', org_key)
        org_desc = org_config.get('description', 'Repository target')
        
        print(f"\n{Colors.MAGENTA}✨ {Colors.YELLOW}Configuration{Colors.NC} 🌈")
        print(f"{Colors.LIME}{git.get_identity_summary()}{Colors.NC}")
        print(f"{Colors.PURPLE}🏢 Target:{Colors.NC} {Colors.GREEN}{org_desc}{Colors.NC}")
        
        # Repository details
        print(f"\nTarget: {Colors.GREEN}{org_desc}{Colors.NC}")
        
        # Confirmation
        print(f"\n{Colors.BG_GOLD}{Colors.GREEN}🍀 ⚠️  CONFIRMATION REQUIRED 💰{Colors.NC}")
        print(f"{Colors.BG_GREEN}You are about to create a repository in: {Colors.GOLD}{org_desc}{Colors.NC}")
        print(f"{Colors.BG_RAINBOW}Identity: {Colors.EMERALD}{git.get_identity_summary()}{Colors.NC}")
        
        confirm = input(f"\nConfirm this is the correct target? [y/N]: ")
        if not confirm.lower().startswith('y'):
            print_error("Repository creation cancelled")
            return
            
        print_success(f"Target confirmed: {org_desc}")
        
        # Get repository details
        repo_name = input("Repository name: ").strip()
        if not repo_name:
            print_error("Repository name cannot be empty")
            return
            
        description = input("Description (optional): ").strip()
        
        make_public = input("Make repository public? [y/N]: ").strip()
        private = not make_public.lower().startswith('y')
        visibility = "private" if private else "public"
        
        # Final confirmation
        print(f"\n{Colors.YELLOW}Repository Details:{Colors.NC}")
        print(f"Name: {repo_name}")
        print(f"Description: {description or '(none)'}")
        print(f"Visibility: {visibility}")
        print(f"Target: {org_desc}")
        
        confirm = input(f"\nCreate this repository? [y/N]: ")
        if not confirm.lower().startswith('y'):
            print_info("Repository creation cancelled")
            return
        
        # Create repository using appropriate creator
        creator = self.create_repository_creator(org_key)
        success, result = creator.create_repository(repo_name, description, private)
        
        if success:
            print_success(f"Repository created: {repo_name}")
            print_info(f"Repository URL: {result}")
            
            # Ask about pushing current directory
            if Path(".git").exists():
                push_current = input("Push current directory to new repository? [y/N]: ")
                if push_current.lower().startswith('y'):
                    self.setup_and_push(org_key, repo_name)
        else:
            print_error(f"Failed to create repository: {result}")
    
    def setup_and_push(self, org_key, repo_name):
        """Set up remote and push to new repository"""
        print_info("Setting up remote and pushing...")
        
        org_config = self.config.config.get('organizations', {}).get(org_key, {})
        git = self.get_git_command(org_key)
        
        # Determine the GitHub username/org for the repo URL
        if org_key == 'personal' or org_config.get('name') == 'personal':
            github_user = org_config.get('github_username', org_config.get('git_user_name', 'unknown'))
            repo_url = f"git@github.com:{github_user}/{repo_name}.git"
        else:
            # For organizations
            github_org = org_config.get('github_org_name', org_key)
            repo_url = f"git@github.com:{github_org}/{repo_name}.git"
        
        print_info(f"Repository URL: {repo_url}")
        
        # Remove existing origin if it exists
        git.remote_remove("origin")
        
        # Add new origin
        success, stdout, stderr = git.remote_add("origin", repo_url)
        if not success:
            print_error(f"Failed to add remote: {stderr}")
            return
        
        # Add, commit and push
        success, stdout, stderr = git.add(".")
        if success:
            success, stdout, stderr = git.commit("Initial commit: Irish gold Swiggit CLI with Python power! 🍀💰")
        
        if success:
            success, stdout, stderr = git.push("origin", "main", set_upstream=True)
            if success:
                print_success("Repository pushed successfully! 🌈")
            else:
                print_error(f"Push failed: {stderr}")
        else:
            print_warning("No changes to commit, but remote is set up")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 swiggit.py create")
        sys.exit(1)
    
    command = sys.argv[1]
    cli = SwiggitCLI()
    
    if command == "create":
        cli.create_repository()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
