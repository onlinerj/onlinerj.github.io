@echo off
echo Setting up Chirpy theme...
echo.

REM Check if Ruby is installed
where ruby >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Ruby is not installed. Please install Ruby 3.0+ first.
    exit /b 1
)

echo Ruby version:
ruby --version
echo.

REM Check if Bundler is installed
where bundle >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Installing Bundler...
    gem install bundler
)

echo Bundler version:
bundle --version
echo.

REM Install dependencies
echo Installing dependencies...
bundle install

echo.
echo Setup complete!
echo.
echo To start the development server, run:
echo    bundle exec jekyll serve
echo.
echo For more information, see START_HERE.md
