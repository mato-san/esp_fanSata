#note make your code modular(devided into parts, that can be reusable in various scenario)
import builtins
import sys
import io
import json

if __name__ == '__main__':


#class bufpy:


    def valuehook(line, buffer = io.StringIO(' ')) -> repr:
        #returns a buffer, internal file in python script
        data = line.any()
        if data == None:
            return

        try:
            #serial output test
            value = int(data)
            sys.stdout.write("Raw Data: {}.".format(value)) 
            buffer.write(value + '\n')
            return buffer

        except UnicodeDecodeError:
            _ = data.encode('utf-8', errors = 'backslashreplace').strip()
            sys.stdout = buffer
            sys.stdout.write(_ + '\n')

            builtins._ = None
            return buffer
        
    def dtypeIdentify(value):
        #checks the data type that can be saved as a JSON file
        dtype_name = type(value).__name__
        if value:
            try:
                for i in len(range(value)):
                    line = json.load(line)
                    print('data type: {}'.format(line))
            
            except json.JSONDecodeError:
                print('Recived invalid JSON:')
            except Exception as e:
                print("Error: {}".fromat(e))
