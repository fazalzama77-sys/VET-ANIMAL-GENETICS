# -*- coding: utf-8 -*-
import os
import shutil
import subprocess

SITE_DIR = r"D:\ANIMAL GENETICS APPLICATION"
APK_PROJECT_DIR = r"D:\ANIMAL GENETICS APK"
DEST_ASSETS = os.path.join(APK_PROJECT_DIR, "app", "src", "main", "assets", "site")
JAVA_HOME = r"D:\ANDROID STUDIO\jbr"

print("1. Synchronizing latest site files into APK assets...")
os.makedirs(DEST_ASSETS, exist_ok=True)

# Copy folders: assets, data, images, js
for folder in ["assets", "data", "images", "js"]:
    src = os.path.join(SITE_DIR, folder)
    dst = os.path.join(DEST_ASSETS, folder)
    print(f"Syncing {folder}...")
    subprocess.run(["robocopy", src, dst, "/MIR", "/NFL", "/NDL", "/NJH", "/NJS", "/NP"], check=False)

# Copy root files
for fname in ["index.html", "manifest.json", "service-worker.js"]:
    src = os.path.join(SITE_DIR, fname)
    dst = os.path.join(DEST_ASSETS, fname)
    shutil.copy2(src, dst)
    print(f"Copied {fname}")

print("Assets synchronization complete.")

# Verify image count in APK assets
theory_images = os.path.join(DEST_ASSETS, "images", "theory")
if os.path.exists(theory_images):
    count = len(os.listdir(theory_images))
    print(f"Verified {count} images in APK assets/site/images/theory!")
else:
    print("WARNING: images/theory not found in destination assets!")

print("2. Building release APK with Gradle...")
env = os.environ.copy()
env["JAVA_HOME"] = JAVA_HOME

gradlew = os.path.join(APK_PROJECT_DIR, "gradlew.bat")
cmd = [gradlew, "assembleRelease", "--no-daemon"]

res = subprocess.run(cmd, cwd=APK_PROJECT_DIR, env=env)
if res.returncode != 0:
    print(f"Gradle build failed with code {res.returncode}")
    exit(res.returncode)

# Copy to root Animal-Genetics.apk
out_apk = os.path.join(APK_PROJECT_DIR, "app", "build", "outputs", "apk", "release", "app-release.apk")
target_apk = os.path.join(APK_PROJECT_DIR, "Animal-Genetics.apk")

if os.path.exists(out_apk):
    shutil.copy2(out_apk, target_apk)
    size_mb = os.path.getsize(target_apk) / (1024 * 1024)
    print(f"SUCCESS! Animal-Genetics.apk updated at {target_apk} ({size_mb:.2f} MB)")
else:
    print(f"ERROR: Expected APK not found at {out_apk}")
