import re
import numpy as np
from functools import reduce

import constants


class PhanTich(object):
    def __init__(self, de_bai):
        self.de_bai = de_bai

    def type_problem(self):
        for pattern in constants.CONST_THTT:
            if self.de_bai.find(pattern) != -1:
                return constants.KIEM_TRA_THTT
        for pattern in constants.CONST_DLTT:
            if self.de_bai.find(pattern) != -1:
                return constants.KIEM_TRA_DLTT
        for pattern in constants.CONST_KTCS:
            if self.de_bai.find(pattern) != -1:
                return constants.KIEM_TRA_CO_SO
        for pattern in constants.CONST_TCS:
            if self.de_bai.find(pattern) != -1:
                return constants.TIM_CO_SO

    def parse_data(self, key):
        if not key:
            return [None, None]

        if key == constants.KIEM_TRA_THTT:
            pattern = ''
            for i, char in enumerate(self.de_bai):
                if char in {'R', 'Real'}:
                    pattern += self.de_bai[i:i + 3]
            self.de_bai = self.de_bai.replace(pattern, '')
            vector_space = self.extract_vector()
            data = {'target': vector_space[0], 'given': vector_space[1:]}
        elif key == constants.KIEM_TRA_DLTT:
            pattern = ''
            for i, char in enumerate(self.de_bai):
                if char in {'R', 'Real'}:
                    pattern += self.de_bai[i:i + 3]
            self.de_bai = self.de_bai.replace(pattern, '')
            vector_space = self.extract_vector()
            data = {'given': vector_space}
        elif key == constants.KIEM_TRA_CO_SO:
            pattern = ''
            for i, char in enumerate(self.de_bai):
                if char in {'R', 'Real'}:
                    pattern += self.de_bai[i:i + 4]
            self.de_bai = self.de_bai.replace(pattern, '')
            vector_space = self.extract_vector()
            space = int(re.findall(r'([+\-]?\d+\.?\d*|[+\-]?\.\d+[+\-]?\d\.\d+[Ee][+\-]\d\d?)', pattern)[0])
            data = {"given": vector_space, "dimR": space}
        elif key == constants.TIM_CO_SO:
            vector_space = self.extract_vector()
            data = {'given': vector_space}
        else:
            return [None, None]
        return [key, data]

    def extract_vector(self):
        process1 = re.split(r"[a-zA-Z]([+\-]?\d+\.?\d*|[+\-]?\.\d+[+\-]?\d\.\d+[Ee][+\-]\d\d?)", self.de_bai)
        if len(process1) == 1:
            process1 = re.split(r'_([+\-]?\d+\.?\d*|[+\-]?\.\d+[+\-]?\d\.\d+[Ee][+\-]\d\d?)', process1[0])
        results = []
        if len(process1) == 1:
            x = re.findall(r'([+\-]?\d+\.?\d*|[+\-]?\.\d+[+\-]?\d\.\d+[Ee][+\-]\d\d?)', process1[0])
            results = x
        else:
            for process in process1:
                process2 = re.split(r"_([+\-]?\d+\.?\d*|[+\-]?\.\d+[+\-]?\d\.\d+[Ee][+\-]\d\d?)", process)
                for path in process2:
                    if len(path) == 1 or path is None:
                        del path
                    else:
                        x = re.findall(r'([+\-]?\d+\.?\d*|[+\-]?\.\d+[+\-]?\d\.\d+[Ee][+\-]\d\d?)', path)
                        results.append(x)

        for result in results:
            if len(result) == 0:
                results.remove(result)

        if type(results[0]) is not str:
            data = reduce(lambda a, b: a + b, results)
        else:
            data = results

        data = [int(string) for string in data]

        num_eq = self.de_bai.count("(")
        if num_eq != 0:
            data = np.array_split(data, num_eq)
            return data
