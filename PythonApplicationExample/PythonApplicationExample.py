import os, csv, json, cmd, string
from os.path import isfile, join 

class MyValidation(cmd.Cmd):
    """Class with functions example."""

    def do_all(self, Null):
        self.do_csv()
        print("end")

    def do_files(self):
        try:
            dirpath = 'csv_files'
            return [f for f in os.listdir(dirpath) if isfile(join(dirpath, f))]
        except Exception as err:
            print("ERROR (do_files): " + str(err))

    def do_help(self, line):
        print("Write in console (files) to load files, (csv) to process all csv, (all) to load and process all csv and return json!")

    def do_csv(self):
        try:
            files = self.do_files()
            dirpath = 'csv_files'
            for f in files:
                print(f)
                filename = dirpath+'/'+f
                if os.path.exists(filename + '.json'):
                    os.remove(filename + '.json')
                with open(dirpath+'/'+f) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    jsonfile = open(filename + '.json','w')
                    line_count = 0
                    for row in csv_reader:
                        json.dump(row, jsonfile)
                        if line_count == 0:
                            print(f'Column names are {", ".join(row)}')
                            line_count += 1
                        else:
                            line_count += 1
                            print(f'Column values are {", ".join(row)}')
                    print(f'Processed {line_count} lines.')
        except Exception as err:
            print("ERROR - (do_csv): " + str(err))
        

    def do_EOF(self, line):
        return True

    def do_clear(self, Null):
        os.system('cls')

if __name__ == '__main__':
    MyValidation().cmdloop()
