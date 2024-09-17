
import pandas as pd
import re

csv_files = [
    r'C:\Users\Acer\Downloads\Assignment 2\Question1\CSV1.csv',
    r'C:\Users\Acer\Downloads\Assignment 2\Question1\CSV2.csv',
    r'C:\Users\Acer\Downloads\Assignment 2\Question1\CSV3.csv',
    r'C:\Users\Acer\Downloads\Assignment 2\Question1\CSV4.csv'
]

output_file =  r'C:\Users\Acer\Downloads\Assignment 2\Question1\rajan.txt'


all_texts = []


text_pattern = re.compile(r'[a-zA-Z\s]+')
 
for file in csv_files:
    try:
      
        df = pd.read_csv(file)

       
        if 'SHORT-TEXT' in df or 'TEXT' in df:
   
            column_name = 'SHORT-TEXT' if 'SHORT-TEXT' in df else 'TEXT'
     
            cleaned_text = df[column_name].astype(str).apply(lambda x: ' '.join(text_pattern.findall(x)))

            all_texts.extend(cleaned_text)

        else:
            print(f"No text column present")

    except Exception as e:
        print(f"Error reading {file}: {e}")


with open(output_file, 'w') as f:
    f.write('\n'.join(all_texts))

print(f"Combined text written to {output_file}")
