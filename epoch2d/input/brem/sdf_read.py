import sdf
import os
import numpy as np
import matplotlib.pyplot as plt

# 获取当前文件夹下的所有 .sdf 文件
sdf_files = sorted([f for f in os.listdir('.') if f.endswith('.sdf')])

# 检查是否有 .sdf 文件
if not sdf_files:
    print("No .sdf files found in the current directory.")
    exit()

# 遍历所有 .sdf 文件并进行可视化
for sdf_file in sdf_files:
    print(f"Processing {sdf_file}...")
    
    # 读取 SDF 文件
    sdf_data = sdf.read(sdf_file)
    
    # 提取需要可视化的变量（例如密度或电场）
    # 这里以 `number_density` 为例，按种类提取
    if 'Grid/Grid_mid' in sdf_data:
        grid = sdf_data['Grid/Grid_mid'].data  # 网格数据
        x, y = grid[0], grid[1]  # x 和 y 方向的网格坐标
    else:
        print(f"Grid data not found in {sdf_file}. Skipping...")
        continue

    if 'Derived/Number_Density/Electron_Beam' in sdf_data:
        density = sdf_data['Derived/Number_Density/Electron_Beam'].data  # 电子束的数密度
    else:
        print(f"Number density data not found in {sdf_file}. Skipping...")
        continue

    # 绘制伪彩图
    plt.figure(figsize=(8, 6))
    plt.pcolormesh(x, y, density.T, shading='auto', cmap='viridis')
    plt.colorbar(label='Number Density')
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.title(f"Number Density - {sdf_file}")
    
    # 保存图片
    output_image = sdf_file.replace('.sdf', '.png')
    plt.savefig(output_image, dpi=300)
    print(f"Saved visualization to {output_image}")
    plt.close()

print("All files processed.")