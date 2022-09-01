import os
import subprocess

input_dir = 'raw_inference_data'
output_dir = 'inference_data'
target_dimension = [620, 460]

def main():

    if len(os.listdir(output_dir)): 
        input(f"Warning: {output_dir} is not empty, hit ENTER to continue\n")
        
    for file_name in os.listdir(input_dir):
        image_name = file_name.split('.')[0]
        image_name_out = image_name + f'_{target_dimension[0]}x{target_dimension[1]}'
        file_name_out = image_name_out + '.png'

        path_to_input_file = os.path.join(input_dir, file_name)
        path_to_output_file = os.path.join(output_dir, file_name_out)

        subprocess.run(['ffmpeg', '-y', '-i', path_to_input_file, '-vf', f'scale={target_dimension[0]}:{target_dimension[1]}', path_to_output_file])

if __name__ == "__main__":
    main()
