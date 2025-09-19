#!/bin/bash

# 🍀 SWIGGIT Global Installer 💰
# One-command install from GitHub

set -e

REPO="uptime-org/swiggit"
INSTALL_DIR="/usr/local/bin"
TEMP_DIR="/tmp/swiggit-install"

echo "🍀 Installing Swiggit - Irish Gold Git CLI 💰"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check if running on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ This installer is for macOS only"
    exit 1
fi

# Check if we have curl
if ! command -v curl >/dev/null 2>&1; then
    echo "❌ curl is required but not installed"
    exit 1
fi

# Check if we have jq
if ! command -v jq >/dev/null 2>&1; then
    echo "📦 Installing jq (required for JSON parsing)..."
    if command -v brew >/dev/null 2>&1; then
        brew install jq
    else
        echo "❌ Homebrew is required to install jq. Please install Homebrew first:"
        echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        exit 1
    fi
fi

# Create temp directory
echo "📁 Creating temporary directory..."
rm -rf "$TEMP_DIR"
mkdir -p "$TEMP_DIR"

# Download the swiggit script from GitHub
echo "⬇️  Downloading Swiggit from GitHub..."
curl -s -L "https://raw.githubusercontent.com/$REPO/main/swiggit" -o "$TEMP_DIR/swiggit"

if [[ ! -f "$TEMP_DIR/swiggit" ]]; then
    echo "❌ Failed to download Swiggit"
    exit 1
fi

# Make executable
chmod +x "$TEMP_DIR/swiggit"

# Check if we need sudo for install
if [[ ! -w "$INSTALL_DIR" ]]; then
    echo "🔐 Installing to $INSTALL_DIR (requires sudo)..."
    sudo cp "$TEMP_DIR/swiggit" "$INSTALL_DIR/swiggit"
else
    echo "📦 Installing to $INSTALL_DIR..."
    cp "$TEMP_DIR/swiggit" "$INSTALL_DIR/swiggit"
fi

# No global config needed - each project brings its own

# Clean up
rm -rf "$TEMP_DIR"

echo ""
echo "🎉 Swiggit installed successfully! 💰🌈"
echo ""
echo "🚀 Quick Start:"
echo "  1. cd into your project directory"
echo "  2. Create .swiggit.json (copy from example)"
echo "  3. Add your GitHub token and SSH key path"
echo "  4. Run: swiggit identity"
echo ""
echo "📚 Commands:"
echo "  swiggit create         - Create repository"
echo "  swiggit identity       - Show identity"
echo "  swiggit add            - Stage files"
echo "  swiggit commit         - Commit changes"
echo "  swiggit push           - Push to remote"
echo "  swiggit pull           - Pull from remote"
echo "  swiggit status         - Git status"
echo "  swiggit rebase         - Interactive rebase"
echo ""
echo "🍀 Happy coding! 💰🌈"