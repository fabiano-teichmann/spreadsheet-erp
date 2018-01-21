import pandas as pd

class LoadFile(object):

    def __init__(self, file_object , sheet):
        """
        Load excel csv
        :param file_object: <bytes>
        :param sheet: <string>
        """

        try:
            dataframe = pd.read_excel(file_object, sheet)

        except:
            try:
                dataframe = pd.read_csv(file_object)

            except Exception as e:
                raise e ('File not supported')

    def header(self, row):
        df = self.dataframe
        header = df.head().values.to_list()
        return  header