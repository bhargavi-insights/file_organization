import streamlit as st
import os
import shutil
import hashlib

UNDO_LOG = "undo_log.txt"

categories = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv"],
    "WordDoc": [".doc", ".docx"]
}


# ---------- FUNCTIONS ---------- #

def create_folder(base, folder):
    folder_path = os.path.join(base, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def undo_operation():
    if os.path.exists(UNDO_LOG):
        with open(UNDO_LOG, "r") as f:
            for line in f:
                src, dest = line.strip().split("|")
                if os.path.exists(dest):
                    shutil.move(dest, src)
        return True
    return False


# ---------- UI ---------- #

st.set_page_config(page_title="Smart File Organizer", layout="centered")

st.title("📂 Smart File Organizer")
st.markdown("Organize your messy folders easily 🚀")

st.divider()

# Step 1: Folder input
st.subheader("📁 Step 1: Enter Folder Path")
path = st.text_input("Enter folder path")

st.divider()

# Step 2: Options
st.subheader("⚙️ Step 2: Select Options")

col1, col2, col3 = st.columns(3)

with col1:
    dry_run = st.checkbox("Dry Run")

with col2:
    delete_duplicates = st.checkbox("Delete Duplicates")

with col3:
    undo_btn = st.button("Undo Last Operation")

# Undo action
if undo_btn:
    if undo_operation():
        st.success("✅ Undo completed successfully!")
    else:
        st.warning("⚠️ No undo data found")

st.divider()

# Step 3: Category selection
st.subheader("📂 Step 3: Select Category")

file_type = st.selectbox(
    "Choose what to organize",
    ["All", "Images", "PDFs", "Videos", "WordDoc"]
)

st.divider()

# Step 4: Run
run = st.button("🚀 Organize Files")


# ---------- MAIN LOGIC ---------- #

if run:

    if not os.path.exists(path):
        st.error("❌ Invalid folder path")
        st.stop()

    files = os.listdir(path)

    hash_map = {}
    duplicates = []
    undo_action = []

    # -------- FIND DUPLICATES -------- #
    for file in files:

        src = os.path.join(path, file)

        if os.path.isdir(src):
            continue

        file_hash = get_file_hash(src)

        if file_hash in hash_map:
            duplicates.append(file)
        else:
            hash_map[file_hash] = file

    # -------- HANDLE DUPLICATES -------- #
    if delete_duplicates:

        create_folder(path, "Duplicate_Deleted")

        for file in duplicates:

            src = os.path.join(path, file)
            dest = os.path.join(path, "Duplicate_Deleted", file)

            if dry_run:
                st.info(f"[DRY RUN] Duplicate → {file}")
            else:
                if os.path.exists(src):
                    shutil.move(src, dest)
                    undo_action.append(f"{src}|{dest}")

        st.success("🗑️ Duplicate files moved to 'Duplicate_Deleted' folder")

    files = os.listdir(path)

    # -------- ORGANIZE FILES -------- #
    organized_count = 0

    for file in files:

        src = os.path.join(path, file)

        if os.path.isdir(src):
            continue

        ext = os.path.splitext(file)[1].lower()
        moved = False

        for folder, extensions in categories.items():

            if file_type != "All" and folder != file_type:
                continue

            if ext in extensions:

                create_folder(path, folder)
                dest = os.path.join(path, folder, file)

                if dry_run:
                    st.info(f"[DRY RUN] {file} → {folder}")
                else:
                    shutil.move(src, dest)
                    undo_action.append(f"{src}|{dest}")

                organized_count += 1
                moved = True
                break

        if not moved and file_type == "All":

            create_folder(path, "Other")
            dest = os.path.join(path, "Other", file)

            if dry_run:
                st.info(f"[DRY RUN] {file} → Other")
            else:
                if os.path.exists(src):
                    shutil.move(src, dest)
                    undo_action.append(f"{src}|{dest}")

            organized_count += 1

    # -------- SAVE UNDO -------- #
    if not dry_run:
        with open(UNDO_LOG, "w") as f:
            for action in undo_action:
                f.write(action + "\n")

    # -------- FINAL MESSAGE -------- #
    if dry_run:
        st.warning("🔍 Dry Run completed (No files moved)")
    else:
        st.success(f"✅ {organized_count} files organized successfully!")

        if file_type != "All":
            st.info(f"📂 {file_type} files organized")
        else:
            st.info("📂 All files organized into categories")