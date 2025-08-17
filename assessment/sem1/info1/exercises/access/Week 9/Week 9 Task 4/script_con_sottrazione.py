#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class Matrix:

    def __init__(self, matrix):
        assert matrix !=[] #matrix can't be an empty list
        assert isinstance(matrix,list) #matrix needs to be of type 'list'

        for sub_list in matrix:
            assert isinstance(sub_list, list) #matrix has to have sublists in the main list
            assert sub_list != [] #the sublists of the matrix can't be empty
            assert len(sub_list) == len(matrix[0]) #matrice non quadrata

            for num in sub_list:
                assert isinstance(num, (int, float)) #i caratteri contenuti nelle sublists della matrice possono essere int o float

        self.__matrix = matrix


    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        else:
            return self.__matrix == other.__matrix

    def __hash__(self):
        return hash(tuple([tuple(sub_list) for sub_list in self.__matrix]))

    def __add__(self, Matrix_2):
        assert isinstance(Matrix_2, Matrix) #check if type of the matrixes is Matrix
        assert isinstance(self.__matrix, list)
        rows = len(Matrix_2.__matrix)
        cols = len(Matrix_2.__matrix[0])
        assert rows == len(self.__matrix)
        assert cols == len(self.__matrix[0])  #se righe e colonne non sono uguali non posso sommare due matrici

        result_of_sum = []

        for i in range(len(self.__matrix)): 
            result_of_sum.append([]) 
            for j in range(len(self.__matrix[0])):
                result_of_sum[i].append(0)
        for i in range(len(self.__matrix)):  
            for j in range(len(self.__matrix[0])):
                result_of_sum[i][j] = self.__matrix[i][j] + Matrix_2.__matrix[i][j]
            
        return Matrix(result_of_sum)

    def __mul__(self,Matrix_2):
        assert isinstance(Matrix_2, Matrix) #check if type of the matrixes is Matrix
        assert isinstance(self.__matrix, list)
        rows = len(self.__matrix)
        cols = len(self.__matrix[0])
        rows_2 = len(Matrix_2.__matrix)
        cols_2 = len(Matrix_2.__matrix[0])
        assert rows == len(self.__matrix)
        assert cols == len(self.__matrix[0])  #se righe e colonne non sono uguali non posso sommare due matrici
        assert rows == cols_2
        assert cols == rows_2

        result_of_mul = []

        for i in range(len(self.__matrix)): 
            result_of_mul.append([]) 
            for j in range(len(self.__matrix[0])):
                result_of_mul[i].append(0)

        for i in range(len(self.__matrix)):
   # iterate through columns of the first matrix
            for j in range(len(Matrix_2.__matrix[0])):
       # iterate through sub_lists of the second matrix
                for k in range(len(Matrix_2.__matrix)):
                    result_of_mul[i][j] += self.__matrix[i][k] * Matrix_2.__matrix[k][j]
        return Matrix(result_of_mul)

    def __repr__(self):
        return repr(self.__matrix)

    def __str__(self):
        return str(self.__matrix)

    def __sub__(self, Matrix_2):
        assert isinstance(Matrix_2, Matrix) #check if type of the matrixes is Matrix
        assert isinstance(self.__matrix, list)
        rows = len(Matrix_2.__matrix)
        cols = len(Matrix_2.__matrix[0])
        assert rows == len(self.__matrix)
        assert cols == len(self.__matrix[0])  #se righe e colonne non sono uguali non posso sommare due matrici

        result_of_sum = []

        for i in range(len(self.__matrix)): 
            result_of_sum.append([]) 
            for j in range(len(self.__matrix[0])):
                result_of_sum[i].append(0)
        for i in range(len(self.__matrix)):  
            for j in range(len(self.__matrix[0])):
                result_of_sum[i][j] = self.__matrix[i][j] - Matrix_2.__matrix[i][j]
            
        return Matrix(result_of_sum)


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    M = Matrix([[5,5],[5,5]])
    T = Matrix([[5,5],[5,4]])
    print(M)
    print(T)
    print(M == T)
    d = {M: "1", T: "2"}
    d.update({M: "3"})
    print(d)
    print(M+T)
    print(M*T)
    print(M-T)
