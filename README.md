# 🍀 Swiggit 💰
**Irish Gold Multi-Organization Git CLI with Identity Management**

## 🚀 One-Command Install

```bash
curl -fsSL https://raw.githubusercontent.com/uptime-org/swiggit/main/install.sh | bash
```

Then in any project directory:
```bash
# Copy example config
curl -fsSL https://raw.githubusercontent.com/uptime-org/swiggit/main/.swiggit.example.json > .swiggit.json

# Edit config with your details
vim .swiggit.json

# Start using Swiggit!
swiggit identity
swiggit status
```

## ✨ Features

- 🍀 **Irish Gold Theme** - Beautiful colors and rainbow animations
- 🔐 **Identity Management** - Per-project SSH keys and git identity
- 🏢 **Multi-Organization Support** - Personal accounts and organizations  
- ✅ **Smart Operations** - Auto-setup remotes, upstream tracking
- ⚠️ **Confirmation Prompts** - Never accidentally push to wrong repo
- 🚀 **Complete Git Workflow** - All commands you need
- 💰 **GitHub Integration** - Create repos via API with tokens

## 📋 Commands

```bash
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

MIT License

---

**🍀 Happy coding with Irish gold! 💰🌈**