import os
import zipfile
import shutil

def unzip_and_move_all(zip_dir, out_dir, delete_zip=False):
    # フォルダがなければ作成
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # zip_dir内の全ZIPを処理
    for filename in os.listdir(zip_dir):
        if filename.lower().endswith('.zip'):
            zip_path = os.path.join(zip_dir, filename)
            extract_folder_name = os.path.splitext(filename)[0]
            extract_path = os.path.join(zip_dir, extract_folder_name)
            
            # ZIP展開
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            
            # 展開フォルダをout_dirへ移動
            target_path = os.path.join(out_dir, extract_folder_name)
            # すでに同名フォルダがある場合、リネームなどで対応可
            if os.path.exists(target_path):
                print(f"警告: {target_path} は既に存在しています。上書きしません。")
            else:
                shutil.move(extract_path, target_path)
                print(f"{extract_folder_name} を {out_dir} に移動しました。")
            
    print("処理が完了しました。")

# 使い方
if __name__ == "__main__":
    zip_folder = r"C:\Users\syuin\WebApp\全自動zip解凍\zip_input"    # ZIPファイルがあるフォルダ
    output_folder = r"C:\Users\syuin\WebApp\全自動zip解凍\zip_output" # 移動先フォルダ
    unzip_and_move_all(zip_folder, output_folder, delete_zip=True) # ZIP削除ならTrue
