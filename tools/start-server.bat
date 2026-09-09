@echo off
cd /d "%~dp0.."
start "Animal Genetics Studio" http://localhost:5179/index.html#/
node tools\local-server.js 5179
