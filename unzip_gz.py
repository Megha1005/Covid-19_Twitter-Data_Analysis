import gzip
import shutil
from pathlib import Path
from tqdm import tqdm

def main():
    data_dirs = ['jsonl/2020-02']
    unzip_gz(data_dirs)

def unzip_gz(data_dirs):
    for data_dir in data_dirs:
        gz_list = list(Path(data_dir).glob('**/*.gz'))
        gz_list_new = []
        for path in gz_list:
            jsonl_path = path.with_suffix('.jsonl')
            if jsonl_path.is_file():
                print('skipping jsonl file already exists: {}'.format(jsonl_path))
                continue
            # unzip
            gz_list_new.append(path)

        print("Unzipping gz giles...")
        invalid_f = 0
        with tqdm(total=len(gz_list_new)) as pbar:
            for path in gz_list_new:
                try: 
                    # with gzip.open(str(path, 'rb')) as f_in:
                    #     with open(str(path.with_suffix('.jsonl')), 'wb') as f_out:
                    #         shutil.copyfileobj(f_in, f_out)

                    input = gzip.GzipFile(str(path), 'rb')
                    s = input.read()
                    input.close()

                    output = open(str(path.with_suffix('.jsonl')), 'wb')
                    output.write(s)
                    output.close()
                except:
                    invalid_f += 1
                pbar.update(1) 


        print("Total files successully unzipped: %i" % (len(gz_list_new)-invalid_f))


if __name__ == '__main__':
    main()