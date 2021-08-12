import os
import argparse
import pandas as pd

# 指定输入参数与信息
parser=argparse.ArgumentParser(description="Simple folder remover.")
parser.add_argument('--manifest','-m',help='Location of gdc manifest file.')
parser.add_argument('--source_folder', '-s',help='Location of folder temporarialy containing GDC sequence data.')
parser.add_argument('--dest_folder', '-d',help='Location of folder officially store GDC sequence data.')
parser.add_argument("--output_log", '-o', help="Log file of moving results")

args=parser.parse_args()

manifest_info = pd.read_table(args.manifest)

if __name__=='__main__':
    with open(args.output_log, 'w') as f:
        # 遍历每个case信息进行剪切操作
        for i in manifest_info.index:
            source_file_loc = os.path.join(args.source_folder, manifest_info['id'][i])
            dest_folder_loc = args.dest_folder
            print(f"Start to move {source_file_loc} into {dest_folder_loc}......")
            # 执行剪切操作，并检查剪切过程是否正常
            execute_status = os.popen(f"mv {source_file_loc} {dest_folder_loc}").read()
            if execute_status == "":
                print("Move successfully.")
                f.write(f"{source_file_loc} has been successfully moved into {args.dest_folder}.\n")
            else:
                print("Move failed.")
                f.write(f"{source_file_loc} failed to move into {args.dest_folder}.\nLog info as followed.")
                f.write(execute_status+"\n")
            

