#!/bin/bash

echo "🎉 Setting up Chirpy theme..."
echo ""

# Check if Ruby is installed
if ! command -v ruby &> /dev/null; then
    echo "❌ Ruby is not installed. Please install Ruby 3.0+ first."
    exit 1
fi

echo "✅ Ruby version: $(ruby --version)"
echo ""

# Check if Bundler is installed
if ! command -v bundle &> /dev/null; then
    echo "📦 Installing Bundler..."
    gem install bundler
fi

echo "✅ Bundler version: $(bundle --version)"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
bundle install

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 To start the development server, run:"
echo "   bundle exec jekyll serve"
echo ""
echo "📖 For more information, see START_HERE.md"
