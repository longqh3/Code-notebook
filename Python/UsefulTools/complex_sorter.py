import pandas as pd

import argparse

parser=argparse.ArgumentParser(description="Complex sorting task.")
# parser.add_argument('--raw_RNA_mutations', '-r' ,choices=[5,10,20],default=5,type=int,help='Number of epochs.')
# Generic parameter
parser.add_argument('--data_info', help='Data info waiting for sorting')
parser.add_argument("--sort_type", help="Type of sorting.")
parser.add_argument("--output_table_path", help="Path for output tables.")

args = parser.parse_args()

# 定义排序函数（以染色体顺序排序）
def Set_Chr_Nr_(all_info):
    """ Sort by chromosome """
    Chr = all_info[0]
    pos = all_info[1]
    if Chr: 
        New = Chr
        if New == 'X': New = 23
        elif New == 'Y': New = 24
        elif New == 'M': New = 25
        else: New = int(New)
    else:
        New = 0
    return(New, pos)


if __name__ == '__main__':
    if args.sort_type == "chr_pos":
        data_info = pd.read_table(args.data_info)
        # 根据染色体和位置信息排序
        ## 提取指定dataframe中所有行的信息
        dataframe_rows_list = [list(i)[1:] for i in data_info.itertuples()]
        data_info = pd.DataFrame(sorted(dataframe_rows_list, key=lambda x: Set_Chr_Nr_(x)), columns=data_info.columns)
        data_info.to_csv(args.output_table_path, sep="\t", index=False)