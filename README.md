# 🔧 SWIGGIT - Multi-Organization Git CLI Tool

**Swiggit** = **S**ecure **W**orkflow, **I**ntegrated **G**it operations with **G**uarded **I**dentity **T**ool

A powerful command-line tool for managing Git operations across multiple organizations with built-in SSH key management, authentication validation, and confirmation prompts.

## ✨ Features

- 🔐 **SSH Key Management** - Centralized SSH key configuration and validation
- 🏢 **Multi-Organization Support** - Easy switching between personal, work, and client organizations  
- ✅ **Authentication Validation** - Proves which account you're connected to before operations
- ⚠️ **Confirmation Prompts** - Never accidentally create repos in the wrong organization
- 🚀 **Automated Workflows** - Commit, push, and repository creation with full context
- 🎨 **Colorized Output** - Clear, visual feedback for all operations

## 🚀 Quick Start

1. **Configure your settings** in `.ssh/.swiggit`
2. **Add your SSH keys** to `.ssh/`
3. **Run commands** with full validation and confirmation

## 📋 Commands

```bash
./swiggit.sh status     # Show repository status and SSH configuration
./swiggit.sh list       # List repositories in your organizations  
./swiggit.sh create     # Create new repository with validation
./swiggit.sh commit     # Commit and push changes with full context
./swiggit.sh help       # Show all available commands
```

## 🔧 Configuration

Edit `.ssh/.swiggit` to configure:
- **Git Identity** (name, email)
- **SSH Settings** (key path, options)
- **Organizations** (with descriptions)
- **Default Settings** (branch, auto-push, etc.)

## 🛡️ Security Features

- **Identity Verification** - Always shows which GitHub account you're authenticated as
- **Organization Validation** - Tests actual access before creating repositories  
- **Explicit Confirmation** - Requires manual confirmation for destructive operations
- **SSH Key Isolation** - Uses project-specific SSH keys with proper options

## 📄 License

MIT License - See LICENSE file for details

---

**Built for secure, multi-organization Git workflows** 🎯# Testing rebase command
