# Swiggit
**Multi-Organization Git CLI with Identity Management**

*A secure command-line tool for managing Git operations across multiple organizations with SSH key isolation and per-project identity management.*

## 🚀 One-Command Install

```bash
curl -fsSL https://raw.githubusercontent.com/uptime-org/swiggit/main/install.sh | bash
```

Then in any project directory:
```bash
# Create config file instantly
swiggit init

# Edit config with your details
vim .swiggit.json

# Start using Swiggit!
swiggit identity
swiggit status
```

## ✨ Features

- 🔐 **Identity Management** - Per-project SSH keys and git identity configuration
- 🏢 **Multi-Organization Support** - Seamlessly work with personal accounts and organizations  
- ✅ **Smart Operations** - Auto-setup remotes, upstream tracking, and validation
- ⚠️ **Safety Features** - Confirmation prompts prevent accidental operations
- 🚀 **Complete Git Workflow** - All essential git operations in one tool
- 🔗 **GitHub Integration** - Create repositories via API with token authentication
- 🌈 **Enhanced UI** - Colorized output with clear visual feedback

## 📋 Commands

```bash
swiggit init           # Create .swiggit.json config file
swiggit identity       # Show current identity
swiggit status         # Git status
swiggit add [files]    # Stage files
swiggit commit [msg]   # Commit changes  
swiggit push           # Smart push (auto-setup remote/upstream)
swiggit pull           # Pull from remote
swiggit rebase         # Interactive rebase
swiggit create         # Create GitHub repository via API
```

## 🔧 Configuration

Each project needs a `.swiggit.json` file:

```json
{
  "organizations": {
    "personal": {
      "name": "personal",
      "description": "Personal GitHub Account",
      "git_user_name": "your-name",
      "git_user_email": "your-email@domain.com",
      "ssh_key_path": "./.ssh/id_rsa",
      "github_username": "your-github-username",
      "github_token": "your_personal_access_token",
      "expected_user": "your-github-username"
    }
  }
}
```

## 🛡️ Security Features

- **Project-Specific Config** - Each project has its own identity
- **SSH Key Isolation** - Uses specified SSH keys with IdentitiesOnly
- **Token-Based API** - No global git configs needed
- **Gitignore Protection** - Config files are automatically ignored
- **Identity Verification** - Shows exactly which account you're using

## 📄 License

MIT License with Non-Commercial Restriction - See [LICENSE](LICENSE) file for details.

**For commercial use, please contact:** uptime.llc.ops@gmail.com

---

**Secure, multi-organization Git workflows made simple.**
