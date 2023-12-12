class Student:
    """Student representa um estudante
    
    Attributes:
        registration_number (str): Número de registro
        name (str): Nome do estudante
        grade (int): Notas do aluno
    """
    
    def __init__(self, registration_number: str, name: str, grade: float):
        
        self.registration_number = registration_number
        self.name = name
        self.grade = grade
        
    @property
    def registration_number(self):
        """(int): Número da matrícula do aluno"""
        return self.__registration_number
        
    @registration_number.setter
    def registration_number(self, registration_number):
        self.__registration_number = registration_number
            
    @property 
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, name):
        self.__name = name
            
    @property
    def grade(self):
        return self.__grade
        
    @grade.setter
    def grade(self, grade):
        self.__grade = grade
        
    def get_media(self) -> float:
        """Retorna a média do aluno"""
        if len(self.__grade) == 0:
            return 0
        return sum(self.__grade) / len(self.__grade)
    
    def get_situacao(self) -> str:
        """Retorna a situação do aluno"""
        media = self.get_media()
        if media >= 7:
            return "Aprovado!"
        elif 5 <= media < 7:
            return "Recuperação!"
        else:
            return "Reprovado!"
        
if __name__ == "__main__":
    grade_student:float = [6.7, 9.8, 5.4, 10, 8.3]
    student = Student(12345, "Lucas", grade_student)
    
    media_student = student.get_media()
    student_situation = student.get_situacao()
    
    print(f"Aluno: {student.name}")
    print(f"Número da matricula: {student.registration_number}")
    print(f"Média total: {media_student:.2f}")
    print(f"Situação: {student_situation}")