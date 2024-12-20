import pyodbc
import flask;
import datetime

app = flask.Flask(__name__)

class Departamento:
    
    def __init__(self):
        self.ID_Departamento = 0  # Valor inicial de ID
        self.Nombre = None  # Valor inicial de Nombre

    def GetId(self) -> int:
        return self.ID_Departamento

    def SetId(self, value: int) -> None:
        self.ID_Departamento = value

    def GetNombre(self) -> str:
        return self.Nombre

    def SetNombre(self, value: str) -> None:
        self.Nombre = value


class Colegio:
    
    id_colegio: int = 0
    nombre: str = None
    direccion: str = None
    telefono: str = None
    id_comuna: int = None
    
    def GetId(self) -> int:
        return self.id_colegio
    
    def SetId(self, value: int) -> None:
        self.id_colegio = value
    
    def GetNombre(self) -> str:
        return self.nombre
    
    def SetNombre(self, value: str) -> None:
        self.nombre = value
    
    def GetDireccion(self) -> str:
        return self.direccion
    
    def SetDireccion(self, value: str) -> None:
        self.direccion = value
    
    def GetTelefono(self) -> str:
        return self.telefono
    
    def SetTelefono(self, value: str) -> None:
        self.telefono = value
    
    def GetComunaId(self) -> int:
        return self.id_comuna
    
    def SetComunaId(self, value: int) -> None:
        self.id_comuna = value


class Rector:
    
    ID_Rector: int = 0
    Nombre: str = None
    Apellido: str = None
    Genero: str = None
    Email: str = None
    Direccion: str = None
    Fecha_contratacion: datetime = None
    Fecha_Nacimiento: datetime = None
    id_Colegio: int = None
    
    def GetId(self) -> int:
        return self.id_director
    
    def SetId(self, value: int) -> None:
        self.id_director = value
    
    def GetNombre(self) -> str:
        return self.nombre
    
    def SetNombre(self, value: str) -> None:
        self.nombre = value
    
    def GetApellido(self) -> str:
        return self.apellido
    
    def SetApellido(self, value: str) -> None:
        self.apellido = value
        
    def GetGenero(self) -> str:
        return self.Genero
    
    def SetGenero(self, value: str) -> None:
        self.Genero = value
    
    def GetEmail(self) -> str:
        return self.email
    
    def SetEmail(self, value: str) -> None:
        self.email = value
        
    def GetDireccion(self) -> str:
        return self.Direccion
    
    def SetDireccion(self, value: str) -> None:
        self.Direccion = value   
        
    def GetFecha_Contratacion(self) -> datetime:
        return self.Fecha_Contratacion
    
    def SetFecha_Contratacion(self, value: datetime) -> None:
        self.Fecha_Contratacion = value
        
    def GetFecha_Nacimiento(self) -> datetime:
        return self.Fecha_Nacimiento
    
    def SetFecha_Nacimiento(self, value: datetime) -> None:
        self.Fecha_Nacimiento = value
    
    def GetId_Colegio(self) -> int:
        return self.id_Colegio
    
    def SetId_Colegio(self, value: int) -> None:
        self.id_Colegio = value


class SecEducacion_Departamental:
    
    id_secretaria: int = 0
    
    def GetId(self) -> int:
        return self.id_secretaria
    
    def SetId(self, value: int) -> None:
        self.id_secretaria = value

    nombre: str = None
    
    def GetNombre(self) -> str:
        return self.nombre
    
    def SetNombre(self, value: str) -> None:
        self.nombre = value

    direccion: str = None
    
    def GetDireccion(self) -> str:
        return self.direccion
    
    def SetDireccion(self, value: str) -> None:
        self.direccion = value

    email: str = None
    
    def GetEmail(self) -> str:
        return self.email
    
    def SetEmail(self, value: str) -> None:
        self.email = value
    
    id_departamento: int = None
    
    def GetDepartamentoId(self) -> int:
        return self.id_departamento
    
    def SetDepartamentoId(self, value: int) -> None:
        self.id_departamento = value

    _departamento: Departamento = None
    
    def GetDepartamento(self) -> Departamento:
        return self._departamento
    
    def SetDepartamento(self, value: Departamento) -> None:
        self._departamento = value

class Comuna:
    
    def __init__(self, id_comuna: int = None, nombre: str = None, id_ciudad: int = None):
        self.id_comuna = id_comuna
        self.nombre = nombre
        self.id_ciudad = id_ciudad

    def GetId(self) -> int:
        return self.id_comuna
    
    def SetId(self, value: int) -> None:
        self.id_comuna = value
    
    def GetNombre(self) -> str:
        return self.nombre
    
    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetID_Ciudad(self) -> str:
        return self.ID_Ciudad
    
    def SetID_Ciudad(self, value: str) -> None:
        self.ID_Ciudad = value


class DirSecretaria_Educacion:
    
    ID_Director: int = 0
    
    def GetID_Director(self) -> int:
        return self.ID_Director
    
    def SetID_Director(self, value: int) -> None:
        self.ID_Director = value
            
    Nombre: str = None
    
    def GetNombre(self) -> str:
        return self.Nombre
    
    def SetNombre(self, value: str) -> None:
        self.Nombre = value
    
    Apellido: str = None
    
    def GetApellido(self) -> str:
        return self.Apellido
    
    def SetApellido(self, value: str) -> None:
        self.Apellido = value
        
    Genero: str = None
    
    def GetGenero(self) -> str:
        return self.Genero
    
    def SetGenero(self, value: str) -> None:
        self.Genero = value
    
    Email: str = None
    
    def GetEmail(self) -> str:
        return self.Email
    
    def SetEmail(self, value: str) -> None:
        self.Email = value
        
    Direccion: str = None
    
    def GetDireccion(self) -> str:
        return self.Direccion
    
    def SetDireccion(self, value: str) -> None:
        self.Direccion = value
    
    Fecha_contratacion: datetime = None
    
    def GetFecha_contratacion(self) -> datetime:
        return self.Fecha_contratación
    
    def SetFecha_contratacion(self, value: datetime) -> None:
        self.Fecha_contratación = value
    
    Fecha_Nacimiento: datetime = None
    
    def GetFecha_Nacimiento(self) -> datetime:
        return self.Fecha_Nacimiento
    
    def SetFecha_Nacimiento(self, value: datetime) -> None:
        self.Fecha_Nacimiento = value
        
    ID_Secretaria: int = 0
    
    def GetID_Secretaria(self) -> int:
        return self.ID_Secretaria
    
    def SetID_Secretaria(self, value: int) -> None:
        self.ID_Secretaria = value
        
    _SecretariaEducacion: SecEducacion_Departamental = None
    
    def GetSecEducacion_Departamental(self) -> SecEducacion_Departamental:
        return self._SecretariaEducacion
    
    def SetSecEducacion_Departamental(self, value: SecEducacion_Departamental) -> None:
        self._SecretariaEducacion = value

        
class  Regional:  
     
    ID_Regional: int = 0
    
    def GetID_Regional(self) -> int:
        return self.ID_Regional
    
    def SetID_Regional(self, value: int) -> None:
        self.ID_Regional = value
        
    Nombre: str = None
    
    def GetNombre(self) -> str:
        return self.Nombre
    
    def SetNombre(self, value: str) -> None:
        self.Nombre = value
        
    ID_Secretaria: int = 0
    
    def GetID_Secretaria(self) -> int:
        return self.ID_Secretaria
    
    def SetID_Secretaria(self, value: int) -> None:
        self.ID_Secretaria = value 
        
    _SecEducacion_Departamental: SecEducacion_Departamental = None
    
    def GetSecEducacion_Departamental(self) -> SecEducacion_Departamental:
        return self._departamento
    
    def SetSecEducacion_Departamental(self, value: Departamento) -> None:
        self._SecEducacion_Departamental = value 

class Dir_Regional:
    
    ID_DirRegional: int = 0
    
    def GetID_DirRegional(self) -> int:
        return self.ID_DirRegional
    
    def SetID_DirRegional(self, value: int) -> None:
        self.ID_DirRegional = value
        
    Nombre: str = None
    
    def GetNombre(self) -> str:
        return self.Nombre
    
    def SetNombre(self, value: str) -> None:
        self.Nombre = value
    
    Apellido: str = None
    
    def GetApellido(self) -> str:
        return self.Apellido
    
    def SetApellido(self, value: str) -> None:
        self.Apellido = value
        
    Genero: str = None
    
    def GetGenero(self) -> str:
        return self.Genero
    
    def SetGenero(self, value: str) -> None:
        self.Genero = value
    
    Email: str = None
    
    def GetEmail(self) -> str:
        return self.Email
    
    def SetEmail(self, value: str) -> None:
        self.Email = value
        
    Direccion: str = None
    
    def GetDireccion(self) -> str:
        return self.Direccion
    
    def SetDireccion(self, value: str) -> None:
        self.Direccion = value
    
    Fecha_contratación: datetime = None
    
    def GetFecha_contratación(self) -> datetime:
        return self.Fecha_contratación
    
    def SetFecha_contratación(self, value: datetime) -> None:
        self.Fecha_contratación = value
    
    Fecha_Nacimiento: datetime = None
    
    def GetFecha_Nacimiento(self) -> datetime:
        return self.Fecha_Nacimiento
    
    def SetFecha_Nacimiento(self, value: datetime) -> None:
        self.Fecha_Nacimiento = value   
    
    ID_Regional: int = 0
    
    def GetID_Regional(self) -> int:
        return self.ID_Regional
    
    def SetID_Regional(self, value: int) -> None:
        self.ID_Regional = value
    
    _Regional: Regional = None
    
    def GetRegional(self) -> Regional:
        return self._departamento
    
    def SetRegional(self, value: Regional) -> None:
        self._Regional = value
    
class Ciudad:
    
    ID_Ciudad: int = 0
    
    def GetID_Ciudad(self) -> int:
        return self.ID_Ciudad
    
    def SetID_Ciudad(self, value: int) -> None:
        self.ID_Ciudad = value
        
    Nombre: str = None
    
    def GetNombre(self) -> str:
        return self.Nombre
    
    def SetNombre(self, value: str) -> None:
        self.Nombre = value
    
    ID_Regional: int = 0
    
    def GetID_Regional(self) -> int:
        return self.ID_Regional
    
    def SetID_Regional(self, value: int) -> None:
        self.ID_Regional = value 
        
    _Regional: Regional = None
    
    def GetRegional(self) -> Regional:
        return self._Regional
    
    def SetRegional(self, value: Regional) -> None:
        self._Regional = value

class Director_Comuna:
    
    ID_Director: int = 0
    
    def GetID_Director(self) -> int:
            return self.ID_Director
        
    def SetID_Director(self, value: int) -> None:
        self.ID_Director = value 
        
    Nombre: str = None
    
    def GetNombre(self) -> str:
        return self.Nombre
    
    def SetNombre(self, value: str) -> None:
        self.Nombre = value
    
    Apellido: str = None
    
    def GetApellido(self) -> str:
        return self.Apellido
    
    def SetApellido(self, value: str) -> None:
        self.Apellido = value
    
    Genero: str = None
    
    def GetGenero(self) -> str:
        return self.Genero
    
    def SetGenero(self, value: str) -> None:
        self.Genero = value
    
    Email: str = None
    
    def GetEmail(self) -> str:
        return self.Email
    
    def SetEmail(self, value: str) -> None:
        self.Email = value
        
    Direccion: str = None
    
    def GetDireccion(self) -> str:
        return self.Direccion
    
    def SetDireccion(self, value: str) -> None:
        self.Direccion = value
    
    Fecha_contratación: datetime = None
    
    def GetFecha_contratación(self) -> datetime:
        return self.Fecha_contratación
    
    def SetFecha_contratación(self, value: datetime) -> None:
        self.Fecha_contratación = value
    
    Fecha_Nacimiento: datetime = None
    
    def GetFecha_Nacimiento(self) -> datetime:
        return self.Fecha_Nacimiento
    
    def SetFecha_Nacimiento(self, value: datetime) -> None:
        self.Fecha_Nacimiento = value   

    ID_Comuna: int = 0
    
    def GetID_Comuna(self) -> int:
        return self.ID_Comuna
    
    def SetID_Comuna(self, value: int) -> None:
        self.ID_Comuna = value 
        
    _comunal: Comuna = None
    
    def GetComuna(self) -> Comuna:
        return self._comunal
    
    def SetComuna(self, value: Comuna) -> None:
        self._comunal = value
        
class Secretaria_Colegio:
    
    ID_Secretaria: int = 0
    
    def GetID_Secretaria(self) -> int:
        return self.ID_Secretaria
    
    def SetID_Secretaria(self, value: int) -> None:
        self.ID_Secretaria = value
    
    Nombre: str = None
    
    def GetNombre(self) -> str:
        return self.Nombre
    
    def SetNombre(self, value: str) -> None:
        self.Nombre = value
    
    Apellido: str = None
    
    def GetApellido(self) -> str:
        return self.Apellido
    
    def SetApellido(self, value: str) -> None:
        self.Apellido = value
    
    Genero: str = None
    
    def GetGenero(self) -> str:
        return self.Genero
    
    def SetGenero(self, value: str) -> None:
        self.Genero = value
    
    Email: str = None
    
    def GetEmail(self) -> str:
        return self.Email
    
    def SetEmail(self, value: str) -> None:
        self.Email = value
    
    Direccion: str = None
    
    def GetDireccion(self) -> str:
        return self.Direccion
    
    def SetDireccion(self, value: str) -> None:
        self.Direccion = value
    
    Fecha_contratación: datetime = None
    
    def GetFecha_contratación(self) -> datetime:
        return self.Fecha_contratación
    
    def SetFecha_contratación(self, value: datetime) -> None:
        self.Fecha_contratación = value
    
    Fecha_Nacimiento: datetime = None
    
    def GetFecha_Nacimiento(self) -> datetime:
        return self.Fecha_Nacimiento
    
    def SetFecha_Nacimiento(self, value: datetime) -> None:
        self.Fecha_Nacimiento = value
        
    ID_Colegio: int = 0
    
    def GetID_Colegio(self) -> int:
        return self.ID_Colegio
    
    def SetID_Colegio(self, value: int) -> None:
        self.ID_Colegio = value
        
    _Colegio: Colegio = None
    
    def GetColegio(self) -> Colegio:
        return self._Colegio
    
    def SetColegio(self, value: Colegio) -> None:
        self._Colegio = value

class Profesor:
    
    ID_Profesor: int = 0
    
    def GetID_Profesor(self) -> int:
        return self.ID_Profesor
    
    def SetID_Profesor(self, value: int) -> None:
        self.ID_Profesor = value
    
    Nombre: str = None
    
    def GetNombre(self) -> str:
        return self.Nombre
    
    def SetNombre(self, value: str) -> None:
        self.Nombre = value
    
    Apellido: str = None
    
    def GetApellido(self) -> str:
        return self.Apellido
    
    def SetApellido(self, value: str) -> None:
        self.Apellido = value
        
    Genero: str = None
    
    def GetGenero(self) -> str:
        return self.Genero
    
    def SetGenero(self, value: str) -> None:
        self.Genero = value
        
    Email: str = None
    
    def GetEmail(self) -> str:
        return self.Email
    
    def SetEmail(self, value: str) -> None:
        self.Email = value
    
    Direccion: str = None
    
    def GetDireccion(self) -> str:
        return self.Direccion
    
    def SetDireccion(self, value: str) -> None:
        self.Direccion = value
    
    Fecha_Nacimiento: datetime = None
    
    def GetFecha_Nacimiento(self) -> datetime:
        return self.Fecha_Nacimiento
    
    def SetFecha_Nacimiento(self, value: datetime) -> None:
        self.Fecha_Nacimiento = value
        
    Titulo: str = None
    
    def GetTitulo(self) -> str:
        return self.Titulo
    
    def SetTitulo(self, value: str) -> None:
        self.Titulo = value    
        
    ID_Colegio: int = 0
    
    def GetID_Colegio(self) -> int:
        return self.ID_Colegio
    
    def SetID_Colegio(self, value: int) -> None:
        self.ID_Colegio = value
            
    _Colegio: Colegio = None
    
    def GetColegio(self) -> Colegio:
        return self._Colegio
    
    def SetColegio(self, value: Colegio) -> None:
        self._Colegio = value
        
        
class Profesor_Colegio:
    
    ID_Profesor: int = 0
    
    def GetID_Profesor(self) -> int:
        return self.ID_Profesor
    
    def SetID_Profesor(self, value: int) -> None:
        self.ID_Profesor = value  
             
    ID_Colegio: int = 0
    
    def GetID_Colegio(self) -> int:
        return self.ID_Colegio
    
    def SetID_Colegio(self, value: int) -> None:
        self.ID_Colegio = value 
        
    Fecha_contratación: datetime = None
    
    def GetFecha_contratación(self) -> datetime:
        return self.Fecha_contratación
    
    def SetFecha_contratación(self, value: datetime) -> None:
        self.Fecha_contratación = value 
        
    _Colegio: Colegio = None
    
    def GetColegio(self) -> Colegio:
        return self._Colegio
    
    def SetColegio(self, value: Colegio) -> None:
        self._Colegio = value
        
        
class Curso:
    
    ID_Curso: int = 0
    
    def GetID_Curso(self) -> int:
        return self.ID_Curso
    
    def SetID_Curso(self, value: int) -> None:
        self.ID_Curso = value   
        
    Nombre: str = None
    
    def GetNombre(self) -> str:
        return self.Nombre
    
    def SetNombre(self, value: str) -> None:
        self.Nombre = value
        
        
    Num_Estudiantes: int = 0
    
    def GetNum_Estudiantes(self) -> int:
        return self.Num_Estudiantes
    
    def SetNum_Estudiantes(self, value: int) -> None:
        self.Num_Estudiantes = value
        
    ID_Colegio: int = 0
    
    def GetID_Colegio(self) -> int:
        return self.ID_Colegio
    
    def SetID_Colegio(self, value: int) -> None:
        self.ID_Colegio = value            
    
    _Colegio: Colegio = None
    
    def GetColegio(self) -> Colegio:
        return self._Colegio
    
    def SetColegio(self, value: Colegio) -> None:
        self._Colegio = value
        
        
class Asignatura:
    
    ID_Asignatura: int = 0
    
    def GetID_Asignatura(self) -> int:
        return self.ID_Asignatura
    
    def SetID_Asignatura(self, value: int) -> None:
        self.ID_Asignatura = value   
        
    Nombre: str = None
    
    def GetNombre(self) -> str:
        return self.Nombre
    
    def SetNombre(self, value: str) -> None:
        self.Nombre = value
        
    ID_Curso: int = 0
    
    def GetID_Curso(self) -> int:
        return self.ID_Curso
    
    def SetID_Curso(self, value: int) -> None:
        self.ID_Curso = value 
        
    _Curso: Curso = None
    
    def GetCurso(self) -> Curso:
        return self._Curso
    
    def SetCurso(self, value: Curso) -> None:
        self._Curso = value

class Profesor_Asignatura:
    
    ID_Profesor: int = 0
    
    def GetID_Profesor(self) -> int:
        return self.ID_Profesor
    
    def SetID_Profesor(self, value: int) -> None:
        self.ID_Profesor = value
        
    ID_Asignatura: int = 0
    
    def GetID_Asignatura(self) -> int:
        return self.ID_Asignatura
    
    def SetID_Asignatura(self, value: int) -> None:
        self.ID_Asignatura = value    
        
    fecha_contratacion: datetime = None
    
    def GetFechaContratacion(self) -> datetime:
        return self.fecha_contratacion
    
    def SetFechaContratacion(self, value: datetime) -> None:
        self.fecha_contratacion = value
        
    _Asignatura: Asignatura = None
    
    def GetAsignatura(self) -> Asignatura:
        return self._Asignatura
    
    def SetAsignatura(self, value: Asignatura) -> None:
        self._Asignatura = value   
        
         
class Estudiante:
    
    ID_Estudiante: int = 0
    
    def GetID_Estudiante(self) -> int:
        return self.ID_Estudiante
    
    def SetID_Estudiante(self, value: int) -> None:
        self.ID_Estudiante = value 
        
    Nombre: str = None
    
    def GetNombre(self) -> str:
        return self.Nombre
    
    def SetNombre(self, value: str) -> None:
        self.Nombre = value
    
    Apellido: str = None
    
    def GetApellido(self) -> str:
        return self.Apellido
    
    def SetApellido(self, value: str) -> None:
        self.Apellido = value
        
    Fecha_Nacimiento: datetime = None
    
    def GetFecha_Nacimiento(self) -> datetime:
        return self.Fecha_Nacimiento
    
    def SetFecha_Nacimiento(self, value: datetime) -> None:
        self.Fecha_Nacimiento = value    
        
    ID_Colegio: int = 0
    
    def GetID_Colegio(self) -> int:
        return self.ID_Colegio
    
    def SetID_Colegio(self, value: int) -> None:
        self.ID_Colegio = value 
        
    _Colegio: Colegio = None
    
    def GetColegio(self) -> Colegio:
        return self._Colegio
    
    def SetColegio(self, value: Colegio) -> None:
        self._Colegio = value
        
class Estudiante_Asignatura:
    
    ID_Estudiante: int = 0
    
    def GetID_Estudiante(self) -> int:
        return self.ID_Estudiante
    
    def SetID_Estudiante(self, value: int) -> None:
        self.ID_Estudiante = value 
        
    ID_Asignatura: int = 0
    
    def GetID_Asignatura(self) -> int:
        return self.ID_Asignatura
    
    def SetID_Asignatura(self, value: int) -> None:
        self.ID_Asignatura = value       
        
    Fecha_matricula: datetime = None
    
    def GetFecha_matricula(self) -> datetime:
        return self.Fecha_matricula
    
    def SetFecha_matricula(self, value: datetime) -> None:
        self.Fecha_matricula = value 
        
    _Asignatura: Asignatura = None
    
    def GetAsignatura(self) -> Asignatura:
        return self._Asignatura
    
    def SetAsignatura(self, value: Asignatura) -> None:
        self._Asignatura = value 
        
  #conexión a la base de datos      
class Conexion:
    strConnection: str = """
        Driver={MySQL ODBC 9.1 Unicode Driver};
        Server=localhost;
        Database=db_colegios;
        PORT=3306;
        user=user_colegios;
        password=Colegios2024"""
         
         
    #1). Call proc Table Departamento 
    #Llamando al procedimiento almacenado que consulta la tabla departamento
    def SeleccionarDepartamento(self) -> None:
        conexion = pyodbc.connect(self.strConnection, autocommit=True)
        consulta: str = "{CALL SeleccionarDepartamento()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_Departamento = []  
        for elemento in cursor:
            depto = Departamento()
            depto.SetId(elemento[0])
            depto.SetNombre(elemento[1])
            Datos_Departamento.append(depto)
            
        cursor.close()
        conexion.close()

        for depto in Datos_Departamento:
            print(f"  Departamento: {depto.GetId()} - {depto.GetNombre()}") 
            
          
    #Llamando al procedimiento almacenado que inserta datos en la tabla departamento       
    def Insertar_Departamento(self, ID_Departamento: int, Nombre: str) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            print(f"ID_Departamento: {ID_Departamento}, Nombre: '{Nombre}'")  
            cursor.execute("CALL InsertarDepartamento(?, ?)", (ID_Departamento, Nombre))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Departamento '{Nombre}' insertado correctamente con ID {ID_Departamento}.")
        except pyodbc.Error as e:
            print(f"Error al insertar el Departamento: {e}")
            
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla departamento   
    def Eliminar_Departamento(self, ID_Departamento: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarDepartamento(?)", (ID_Departamento))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Departamento con ID {ID_Departamento} eliminado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar el departamento: {e}")
            
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla departamento   
    def Actualizar_Departamento(self, ID_Departamento: int, NuevoNombre: str) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarDepartamento(?, ?)", (ID_Departamento, NuevoNombre))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Departamento con ID {ID_Departamento} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar el departamento: {e}")
            
            
    #2). Call proc Table SecEducacion_Departamental
    #Llamando al procedimiento almacenado que consulta la tabla SecEducacion_Departamental
    def Seleccionar_SecEducacion_Departamental(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarSecEducacion_Departamental()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_SecEducacionDeparta = []  
        for elemento in cursor:
            SecEdu = SecEducacion_Departamental()
            SecEdu.SetId(elemento[0])
            SecEdu.SetNombre(elemento[1])
            SecEdu.SetDireccion(elemento[2])
            SecEdu.SetEmail(elemento[3])
            SecEdu.SetDepartamento(elemento[4])
            Datos_SecEducacionDeparta.append(SecEdu)
            
        cursor.close()
        conexion.close()

        for SecEdu in Datos_SecEducacionDeparta:
            print(f" Secretaria de Educacion: {SecEdu.GetId()} - {SecEdu.GetNombre()} - {SecEdu.GetDireccion()} - {SecEdu.GetEmail()} - {SecEdu.GetDepartamento()}")
             
    
    #Llamando al procedimiento almacenado que inserta datos en la tabla SecEducacion_Departamental       
    def Insertar_SecEducacion_Departamental(self, ID_Secretaria: int, Nombre: str, Direccion: str, Email: str, ID_Departamento: int) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarSecEducacion_Departamental(?, ?, ?, ?, ?)", (ID_Secretaria, Nombre, Direccion, Email, ID_Departamento  ))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Secretaría de educación departamental {Nombre} con dirección {Direccion} e Email {Email} insertado correctamente con ID {ID_Secretaria}.")
        except pyodbc.Error as e:
            print(f"Error al insertar el Departamento: {e}")
            
                  
    #Llamando al procedimiento almacenado que Elimina datos en la tabla SecEducacion_Departamental   
    def Eliminar_SecEducacion_Departamental(self, ID_Secretaria: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarSecEducacion_Departamental(?)", (ID_Secretaria))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Secretaría de educación departamental, con ID {ID_Secretaria} eliminado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar la Secretaría de educación Educacion: {e}")    
                      
    
    #Llamando al procedimiento almacenado que actualiza datos en la tabla SecEducacion_Departamental   
    def Actualizar_SecEducacion_Departamental(self,ID_Secretaria: int, NuevoNombre: str, NuevaDireccion: str, NuevoEmail: str, NuevoIdDepartamento: int) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarSecEducacion_Departamental(?, ?, ?, ?, ?)", (ID_Secretaria, NuevoNombre, NuevaDireccion, NuevoEmail, NuevoIdDepartamento))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Secretaría de educación departamental con ID {ID_Secretaria} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar la secretaría de educación: {e}")    
            
    
    #3). Call proc Table DirSecretaria_Educacion
    #Llamando al procedimiento almacenado que consulta la tabla DirSecretaria_Educacion
    def Seleccionar_DirSecretaria_Educacion(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarDirSecretaria_Educacion()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_DirSecretaria_Educacion = []  
        for elemento in cursor:
            DirSecEdu = DirSecretaria_Educacion()
            DirSecEdu.SetID_Director(elemento[0])
            DirSecEdu.SetNombre(elemento[1])
            DirSecEdu.SetApellido(elemento[2])
            DirSecEdu.SetGenero(elemento[3])
            DirSecEdu.SetEmail(elemento[4])
            DirSecEdu.SetDireccion(elemento[5])
            DirSecEdu.SetFecha_contratacion(elemento[6])
            DirSecEdu.SetFecha_Nacimiento(elemento[7])
            DirSecEdu.SetID_Secretaria(elemento[8])
            Datos_DirSecretaria_Educacion.append(DirSecEdu)
            
        cursor.close()
        conexion.close()

        for DirSecEdu in Datos_DirSecretaria_Educacion:
            print(f" Director Secretaria de Educacion: {DirSecEdu.GetID_Director()}- {DirSecEdu.GetNombre()} - {DirSecEdu.GetApellido()} - {DirSecEdu.GetGenero()} - {DirSecEdu.GetEmail()}") 
            print(f"{DirSecEdu.GetDireccion()} - {DirSecEdu.GetFecha_contratacion()} - {DirSecEdu.GetFecha_Nacimiento()} - {DirSecEdu.GetID_Secretaria()}  ")
    
    #Llamando al procedimiento almacenado que inserta datos en la tabla DirSecretaria_Educacion       
    def Insertar_DirSecEducacion_Departamental(self, ID_Director: int, Nombre: str, Apellido: str, Genero: str, Email: str, Direccion: str, Fecha_contratación: datetime, Fecha_Nacimiento: datetime, ID_Secretaria: int) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarDirSecretaria_Educacion(?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID_Director, Nombre, Apellido, Genero, Email, Direccion, Fecha_contratación,  Fecha_Nacimiento, ID_Secretaria))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Director Secretaría de educación : {Nombre}  {Apellido}, genero: {Genero}, con fecha de contratacion: {Fecha_contratación}, con fecha de nacimiento : {Fecha_Nacimiento}, con dirección {Direccion}, e Email {Email}. insertado correctamente con ID {ID_Secretaria}.")
        except pyodbc.Error as e:
            print(f"Error al insertar el Departamento: {e}")
                  
    #Llamando al procedimiento almacenado que Elimina datos en la tabla DirSecEducacion_Departamental   
    def Eliminar_DirSecEducacion_Departamental(self, ID_Director: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarDirSecretaria_Educacion(?)", (ID_Director))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Director Secretaría de educación departamental, con ID {ID_Director} eliminado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar Director Secretaría de educación: {e}")    
                      
    
    #Llamando al procedimiento almacenado que actualiza datos en la tabla DirSecEducacion_Departamental   
    def Actualizar_DirSecEducacion_Departamental(self,ID_Director: int, NuevoNombre: str, NuevoApellido: str, NuevoGenero: str, NuevoEmail: str, NuevaDireccion: str, NuevaFecha_contratación: datetime, NuevaFecha_Nacimiento: datetime, NuevaID_Secretaria: int) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarDirSecretaria_Educacion(?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID_Director, NuevoNombre, NuevoApellido, NuevoGenero, NuevoEmail, NuevaDireccion, NuevaFecha_contratación, NuevaFecha_Nacimiento, NuevaID_Secretaria))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Director Secretaría de educación departamental con ID {ID_Director} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Director secretaría de educación: {e}")    
            
    #4). Call proc Table Regional
    #Llamando al procedimiento almacenado que consulta la tabla Regional
    
    def Seleccionar_Regional(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarRegional()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_Regional = []  
        for elemento in cursor:
            datRegional = Regional()
            datRegional.SetID_Regional(elemento[0])
            datRegional.SetNombre(elemento[1])
            datRegional.SetID_Secretaria(elemento[2])
            Datos_Regional.append(datRegional)
            
        cursor.close()
        conexion.close()

        for datRegional in Datos_Regional:
            print(f" Regional: {datRegional.GetID_Regional()}- {datRegional.GetNombre()} - {datRegional.GetID_Secretaria()}") 
            
    #Llamando al procedimiento almacenado que inserta datos en la tabla Regional       
    def Insertar_Regional(self, ID_Regional: int, Nombre: str, ID_Secretaria: int) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarRegional(?, ?, ?)", (ID_Regional, Nombre, ID_Secretaria))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Regional : {Nombre}, con ID: {ID_Regional}, Y ID secretaría: {ID_Secretaria}")
        except pyodbc.Error as e:
            print(f"Error al insertar Regional: {e}")
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla Regional   
    def Eliminar_Regional(self, ID_Regional: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarRegional(?)", (ID_Regional))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Regional, con ID {ID_Regional} eliminada correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar regional: {e}")
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla Regional   
    def Actualizar_Regional(self,ID_Regional: int, NuevoNombre: str, NuevaID_Secretaria: int) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarRegional(?, ?, ?)", (ID_Regional, NuevoNombre,  NuevaID_Secretaria))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Regional con ID {ID_Regional} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Regional: {e}") 
            
    #5). Call proc Table DirRegional
    #Llamando al procedimiento almacenado que consulta la tabla DirRegional
    
    def Seleccionar_DirRegional(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarDirRegional()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_DirRegional = []  
        for elemento in cursor:
            DirRegional = Dir_Regional()
            DirRegional.SetID_DirRegional(elemento[0])
            DirRegional.SetNombre(elemento[1])
            DirRegional.SetApellido(elemento[2])
            DirRegional.SetGenero(elemento[3])
            DirRegional.SetEmail(elemento[4])
            DirRegional.SetDireccion(elemento[5])
            DirRegional.SetFecha_contratación(elemento[6])
            DirRegional.SetFecha_Nacimiento(elemento[7])
            DirRegional.SetID_Regional(elemento[0])
            Datos_DirRegional.append(DirRegional)
            
        cursor.close()
        conexion.close()

        for DirRegional in Datos_DirRegional:
            print(f" Director Regional: {DirRegional.GetID_DirRegional()}- {DirRegional.GetNombre()} - {DirRegional.GetApellido()} - {DirRegional.GetGenero()} - {DirRegional.GetEmail()}") 
            print(f" {DirRegional.GetDireccion()} - {DirRegional.GetFecha_contratación()} - {DirRegional.GetFecha_Nacimiento()} - {DirRegional.GetID_Regional()}")
    
    #Llamando al procedimiento almacenado que inserta datos en la tabla DirRegional      
    def Insertar_DirRegional(self, ID_DirRegional: int, Nombre: str, Apellido: str, Genero: str, Email: str, Direccion: str, Fecha_contratacion: datetime, Fecha_Nacimiento: datetime, ID_Regional: int) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarDirRegional(?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID_DirRegional, Nombre, Apellido, Genero, Email, Direccion, Fecha_contratacion, Fecha_Nacimiento, ID_Regional))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Director Regional : {Nombre}, con ID: {ID_DirRegional}, insertado correctamente")
        except pyodbc.Error as e:
            print(f"Error al insertar Director Regional: {e}")
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla DirRegional   
    def Eliminar_DirRegional(self, ID_DirRegional: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarDirRegional(?)", (ID_DirRegional))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Director Regional, con ID { ID_DirRegional} eliminado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar Director regional: {e}")
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla Regional   
    def Actualizar_DirRegional(self,ID_DirRegional: int, NuevoNombre: str, NuevoApellido: str, NuevoGenero: str, NuevoEmail: str, NuevoDireccion: str, NuevoFecha_contratacion: datetime, NuevoFecha_Nacimiento: datetime, NuevoID_Regional: int) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarDirRegional(?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID_DirRegional, NuevoNombre, NuevoApellido, NuevoGenero, NuevoEmail, NuevoDireccion, NuevoFecha_contratacion, NuevoFecha_Nacimiento, NuevoID_Regional))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Director Regional con ID {ID_DirRegional} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Director Regional: {e}") 
            
    #6). Call proc Table Ciudad
    #Llamando al procedimiento almacenado que consulta la tabla Ciudad
    def Seleccionar_Ciudad(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarCiudad()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_Ciudad = []  
        for elemento in cursor:
            dCiudad = Ciudad()
            dCiudad.SetID_Ciudad(elemento[0])
            dCiudad.SetNombre(elemento[1])
            dCiudad.SetID_Regional(elemento[2])
            Datos_Ciudad.append(dCiudad)
            
        cursor.close()
        conexion.close()

        for dCiudad in Datos_Ciudad:
            print(f" Ciudad: {dCiudad.GetID_Ciudad()}- {dCiudad.GetNombre()} - {dCiudad.GetID_Regional()}") 
            
    #Llamando al procedimiento almacenado que inserta datos en la tabla Ciudad     
    def Insertar_Ciudad(self, ID_Ciudad: int, Nombre: str, ID_Regional: str) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarCiudad(?, ?, ?)", (ID_Ciudad, Nombre, ID_Regional))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Ciudad : {Nombre}, con ID: {ID_Ciudad}, insertado correctamente")
        except pyodbc.Error as e:
            print(f"Error al insertar Ciudad: {e}")
    
     #Llamando al procedimiento almacenado que Elimina datos en la tabla Ciudad  
    def Eliminar_Ciudad(self, ID_Ciudad: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarCiudad(?)", (ID_Ciudad))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Ciudad, con ID {ID_Ciudad} eliminada correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar Ciudad: {e}")
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla Ciudad  
    def Actualizar_Ciudad(self,ID_Ciudad: int, NuevoNombre: str, NuevoID_Regional: int) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarCiudad(?, ?, ?)", (ID_Ciudad, NuevoNombre, NuevoID_Regional))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Ciudad con ID {ID_Ciudad} actualizada correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Ciudad: {e}") 
            
            
    #7). Call proc Table Comuna
    #Llamando al procedimiento almacenado que consulta la tabla Comuna
    def Seleccionar_Comuna(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarComuna()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_Comuna = []  
        for elemento in cursor:
            dComuna = Comuna()
            dComuna.SetId(elemento[0])
            dComuna.SetNombre(elemento[1])
            dComuna.SetID_Ciudad(elemento[2])
            Datos_Comuna.append(dComuna)
            
        cursor.close()
        conexion.close()

        for dComuna in Datos_Comuna:
            print(f" Comuna: {dComuna.GetId()}- {dComuna.GetNombre()} - {dComuna.GetID_Ciudad()}") 
            
     #Llamando al procedimiento almacenado que inserta datos en la tabla Comuna    
    def Insertar_Comuna(self, ID_Comuna: int, Nombre: str, ID_Ciudad: str) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarComuna(?, ?, ?)", (ID_Comuna, Nombre, ID_Ciudad))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Comuna : {Nombre}, con ID: {ID_Comuna}, insertada correctamente")
        except pyodbc.Error as e:
            print(f"Error al insertar Comuna: {e}")
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla Comuna 
    def Eliminar_Comuna(self, ID_Comuna: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarComuna(?)", (ID_Comuna))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Comuna, con ID {ID_Comuna} eliminada correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar Comuna: {e}")
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla Comuna 
    def Actualizar_Comuna(self,ID_Comuna: int, NuevoNombre: str, NuevoID_Ciudad: int) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarComuna(?, ?, ?)", (ID_Comuna, NuevoNombre, NuevoID_Ciudad))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Comuna con ID {ID_Comuna} actualizada correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Comuna: {e}") 
            
    
    #8). Call proc Table director comuna
    #Llamando al procedimiento almacenado que consulta la tabla director comuna
    
    def Seleccionar_DirComuna(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarDirectorComuna()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_DirComuna = []  
        for elemento in cursor:
            DirComuna = Director_Comuna()
            DirComuna.SetID_Director(elemento[0])
            DirComuna.SetNombre(elemento[1])
            DirComuna.SetApellido(elemento[2])
            DirComuna.SetGenero(elemento[3])
            DirComuna.SetEmail(elemento[4])
            DirComuna.SetDireccion(elemento[5])
            DirComuna.SetFecha_contratación(elemento[6])
            DirComuna.SetFecha_Nacimiento(elemento[7])
            DirComuna.SetID_Comuna(elemento[8])
            Datos_DirComuna.append(DirComuna)
            
        cursor.close()
        conexion.close()

        for DirComuna in Datos_DirComuna:
            print(f" Director Comuna: {DirComuna.GetID_Director()}- {DirComuna.GetNombre()} - {DirComuna.GetApellido()} - {DirComuna.GetGenero()} - {DirComuna.GetEmail()}") 
            print(f" {DirComuna.GetDireccion()} - {DirComuna.GetFecha_contratación()} - {DirComuna.GetFecha_Nacimiento()} - {DirComuna.GetID_Comuna()}")
            
    #Llamando al procedimiento almacenado que inserta datos en la tabla DirComuna    
    def Insertar_DirectorComuna(self, ID_Director: int, Nombre: str, Apellido: str, Genero: str, Email: str, Direccion: str, Fecha_contratación: datetime, Fecha_Nacimiento: datetime, ID_Comuna: int) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarDirectorComuna(?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID_Director, Nombre, Apellido, Genero, Email, Direccion, Fecha_contratación, Fecha_Nacimiento, ID_Comuna))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"  Director Comuna : {Nombre}, con ID: {ID_Director}, insertado correctamente")
        except pyodbc.Error as e:
            print(f"Error al insertar Director Comuna: {e}")
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla Director Comuna 
    def Eliminar_DirectorComuna(self, ID_Director: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarDirectorComuna(?)", (ID_Director))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Director Comuna, con ID {ID_Director} eliminado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar Director Comuna: {e}")
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla DirComuna 
    def Actualizar_DirComuna(self, ID_Director: int, NuevoNombre: str, NuevoApellido: str, NuevoGenero: str, NuevoEmail: str, NuevoDireccion: str, NuevoFecha_contratación: datetime, NuevoFecha_Nacimiento: datetime, NuevoID_Comuna: int) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarDirectorComuna(?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID_Director, NuevoNombre, NuevoApellido, NuevoGenero, NuevoEmail, NuevoDireccion, NuevoFecha_contratación, NuevoFecha_Nacimiento, NuevoID_Comuna))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Director Comuna con ID {ID_Director} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Director Comuna: {e}") 
            
            
    #9). Call proc Table colegio
    #Llamando al procedimiento almacenado que consulta la tabla Colegio
    def Seleccionar_Colegio(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarColegio()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_Colegio = []  
        for elemento in cursor:
            dtColegio = Colegio()
            dtColegio.SetId(elemento[0])
            dtColegio.SetNombre(elemento[1])
            dtColegio.SetDireccion(elemento[2])
            dtColegio.SetTelefono(elemento[3])
            dtColegio.SetComunaId(elemento[4])
            Datos_Colegio.append(dtColegio)
            
        cursor.close()
        conexion.close()

        for dtColegio in Datos_Colegio:
            print(f" Colegio: {dtColegio.GetId()}- {dtColegio.GetNombre()} - {dtColegio.GetDireccion()} - {dtColegio.GetTelefono()} - {dtColegio.GetComunaId()}") 
            
     #Llamando al procedimiento almacenado que inserta datos en la tabla Colegio      
    def Insertar_Colegio(self, ID_Colegio: int, Nombre: str, Direccion: str, Telefono: str, ID_Comuna: int) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarColegio(?, ?, ?, ?, ?)", (ID_Colegio, Nombre, Direccion, Telefono, ID_Comuna))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Colegio: {Nombre}, con ID: {ID_Colegio}, insertado correctamente")
        except pyodbc.Error as e:
            print(f"Error al insertar Colegio: {e}")
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla Colegio 
    def Eliminar_Colegio(self, ID_Colegio: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarColegio(?)", (ID_Colegio))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Colegio, con ID {ID_Colegio} eliminado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar Colegio: {e}")
            
     #Llamando al procedimiento almacenado que actualiza datos en la tabla Colegio 
    def Actualizar_Colegio(self, ID_Colegio: int, Nombre: str, Direccion: str, Telefono: str, ID_Comuna: int) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarColegio(?, ?, ?, ?, ?)", (ID_Colegio, Nombre, Direccion, Telefono, ID_Comuna))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Colegio con ID {ID_Colegio} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Colegio: {e}")
            
            
    #10). Call proc Table Rector
    #Llamando al procedimiento almacenado que consulta la tabla Rector
    
    def Seleccionar_Rector(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarRector()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_Rector = []  
        for elemento in cursor:
            dtRector = Rector()
            dtRector.SetId(elemento[0])
            dtRector.SetNombre(elemento[1])
            dtRector.SetApellido(elemento[2])
            dtRector.SetGenero(elemento[3])
            dtRector.SetEmail(elemento[4])
            dtRector.SetDireccion(elemento[5])
            dtRector.SetFecha_Contratacion(elemento[6])
            dtRector.SetFecha_Nacimiento(elemento[7])
            dtRector.SetId_Colegio(elemento[8])
            Datos_Rector.append(dtRector)
            
        cursor.close()
        conexion.close()

        for dtRector in Datos_Rector:
            print(f" Rector: {dtRector.GetId()}- {dtRector.GetNombre()} - {dtRector.GetApellido()} - {dtRector.GetGenero()} - {dtRector.GetEmail()}") 
            print(f" {dtRector.GetDireccion()} - {dtRector.GetFecha_Contratacion()} - {dtRector.GetFecha_Nacimiento()} - {dtRector.GetId_Colegio()}")
            
    #Llamando al procedimiento almacenado que inserta datos en la tabla Rector   
    def Insertar_Rector(self, ID_Rector: int, Nombre: str, Apellido: str, Genero: str, Email: str, Direccion: str, Fecha_contratación: datetime, Fecha_Nacimiento: datetime, ID_Colegio: int) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarRector(?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID_Rector, Nombre, Apellido, Genero, Email, Direccion, Fecha_contratación, Fecha_Nacimiento, ID_Colegio))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f" Rector : {Nombre}, con ID: {ID_Rector}, insertado correctamente")
        except pyodbc.Error as e:
            print(f"Error al insertar Rector: {e}")
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla Rector
    def Eliminar_Rector(self, ID_Rector: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarRector(?)", (ID_Rector))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Rector, con ID {ID_Rector} eliminado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar Rector: {e}")
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla Rector   
    def Actualizar_Rector(self, ID_Rector: int, NuevoNombre: str, NuevoApellido: str, NuevoGenero: str, NuevoEmail: str, NuevoDireccion: str, NuevoFecha_contratacion: datetime, NuevoFecha_Nacimiento: datetime, NuevoID_Colegio: int) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarDirRegional(?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID_Rector, NuevoNombre, NuevoApellido, NuevoGenero, NuevoEmail, NuevoDireccion, NuevoFecha_contratacion, NuevoFecha_Nacimiento, NuevoID_Colegio))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Rector con ID {ID_Rector} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Rector: {e}") 
            
    
    #11). Call proc Table Secretaria_Colegio
    #Llamando al procedimiento almacenado que consulta la tabla Secretaria_Colegio
    
    def Seleccionar_SecretariaColegio(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarSecretariaColegio()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_SecretariaColegio = []  
        for elemento in cursor:
            SecColegio = Secretaria_Colegio()
            SecColegio.SetID_Secretaria(elemento[0])
            SecColegio.SetNombre(elemento[1])
            SecColegio.SetApellido(elemento[2])
            SecColegio.SetGenero(elemento[3])
            SecColegio.SetEmail(elemento[4])
            SecColegio.SetDireccion(elemento[5])
            SecColegio.SetFecha_contratación(elemento[6])
            SecColegio.SetFecha_Nacimiento(elemento[7])
            SecColegio.SetID_Colegio(elemento[8])
            Datos_SecretariaColegio.append(SecColegio)
            
        cursor.close()
        conexion.close()

        for SecColegio in Datos_SecretariaColegio:
            print(f" Secretaria colegio: {SecColegio.GetID_Secretaria()}- {SecColegio.GetNombre()} - {SecColegio.GetApellido()} - {SecColegio.GetGenero()} - {SecColegio.GetEmail()}") 
            print(f" {SecColegio.GetDireccion()} - {SecColegio.GetFecha_contratación()} - {SecColegio.GetFecha_Nacimiento()} - {SecColegio.GetID_Colegio()}")
            
    #Llamando al procedimiento almacenado que inserta datos en la tabla Secretaria_Colegio 
    def Insertar_SecretariaColegio(self, ID_Secretaria: int, Nombre: str, Apellido: str, Genero: str, Email: str, Direccion: str, Fecha_contratacion: datetime, Fecha_Nacimiento: datetime, ID_Colegio: int) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarSecretariaColegio(?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID_Secretaria, Nombre, Apellido, Genero, Email, Direccion, Fecha_contratacion, Fecha_Nacimiento, ID_Colegio))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f" Secretaria colegio : {Nombre}, con ID: {ID_Secretaria}, insertado correctamente")
        except pyodbc.Error as e:
            print(f"Error al insertar Secretaria colegio: {e}")
            
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla Secretaria_Colegio
    def Eliminar_SecretariaColegio(self, ID_Secretaria: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarSecretariaColegio(?)", (ID_Secretaria))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Secretaria Colegio, con ID {ID_Secretaria} eliminad@ correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar Secretaria Colegio: {e}")
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla Secretaria_Colegio   
    def Actualizar_SecretariaColegio(self, ID_Secretaria: int, NuevoNombre: str, NuevoApellido: str, NuevoGenero: str, NuevoEmail: str, NuevoDireccion: str, NuevoFecha_contratacion: datetime, NuevoFecha_Nacimiento: datetime, NuevoID_Colegio: int) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarSecretariaColegio(?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID_Secretaria, NuevoNombre, NuevoApellido, NuevoGenero, NuevoEmail, NuevoDireccion, NuevoFecha_contratacion, NuevoFecha_Nacimiento, NuevoID_Colegio))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Secretaria Colegio con ID {ID_Secretaria} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Secretaria Colegio: {e}")
            
    
    #12). Call proc Table profesor
    #Llamando al procedimiento almacenado que consulta la tabla profesor
    
    def Seleccionar_Profesor(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarProfesor()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_Profesor = []  
        for elemento in cursor:
            dtProfesor = Profesor()
            dtProfesor.SetID_Profesor(elemento[0])
            dtProfesor.SetNombre(elemento[1])
            dtProfesor.SetApellido(elemento[2])
            dtProfesor.SetGenero(elemento[3])
            dtProfesor.SetEmail(elemento[4])
            dtProfesor.SetDireccion(elemento[5])
            dtProfesor.SetFecha_Nacimiento(elemento[6])
            dtProfesor.SetTitulo(elemento[7])
            dtProfesor.SetID_Colegio(elemento[8])
            Datos_Profesor.append(dtProfesor)
            
        cursor.close()
        conexion.close()

        for dtProfesor in Datos_Profesor:
            print(f" Profesor: {dtProfesor.GetID_Profesor()}- {dtProfesor.GetNombre()} - {dtProfesor.GetApellido()} - {dtProfesor.GetGenero()} - {dtProfesor.GetEmail()}") 
            print(f" {dtProfesor.GetDireccion()} - {dtProfesor.GetFecha_Nacimiento()} - {dtProfesor.GetTitulo()}- {dtProfesor.GetID_Colegio()}")
            
    #Llamando al procedimiento almacenado que inserta datos en la tabla profesor
    def Insertar_Profesor(self, ID_Profesor : int, Nombre: str, Apellido: str, Genero: str, Email: str, Direccion: str, Fecha_Nacimiento: datetime, Titulo: str, ID_Colegio: int) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarSecretariaColegio(?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID_Profesor, Nombre, Apellido, Genero, Email, Direccion, Fecha_Nacimiento, Titulo, ID_Colegio))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f" Profesor : {Nombre}, con ID: {ID_Profesor}, insertado correctamente")
        except pyodbc.Error as e:
            print(f"Error al insertar Profesor: {e}")
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla Profesor
    def Eliminar_Profesor(self, ID_Profesor: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarProfesor(?)", (ID_Profesor))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Profesor, con ID {ID_Profesor} eliminado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar Profesor: {e}")
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla profesor  
    def Actualizar_Profesor(self, ID_Profesor: int, NuevoNombre: str, NuevoApellido: str, NuevoGenero: str, NuevoEmail: str, NuevoDireccion: str, NuevoFecha_Nacimiento: datetime, NuevoTitulo:str, NuevoID_Colegio: int) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarProfesor(?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID_Profesor, NuevoNombre, NuevoApellido, NuevoGenero, NuevoEmail, NuevoDireccion, NuevoFecha_Nacimiento, NuevoTitulo, NuevoID_Colegio))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Profesor con ID {ID_Profesor} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar profesor: {e}")
            
            
    #13). Call proc Table Profesor-Colegio
    #Llamando al procedimiento almacenado que consulta la tabla Profesor-Colegio
    def Seleccionar_ProfesorColegio(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarProfesorColegio()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_ProfesorColegio = []  
        for elemento in cursor:
            pro_col = Profesor_Colegio()
            pro_col.SetID_Profesor(elemento[0])
            pro_col.SetID_Colegio(elemento[1])
            pro_col.SetFecha_contratación(elemento[2])
            Datos_ProfesorColegio.append(pro_col)
            
        cursor.close()
        conexion.close()

        for pro_col in Datos_ProfesorColegio:
            print(f"Colegio-profesor: {pro_col.GetID_Profesor()} - {pro_col.GetID_Colegio()} - {pro_col.GetFecha_contratación()}") 
            
    #Llamando al procedimiento almacenado que inserta datos en la tabla profesor - Colegio
    def Insertar_ProfesorColegio(self, ID_Profesor : int, ID_Colegio: int, Fecha_Contratacion: datetime) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarProfesorColegio(?, ?, ?)", (ID_Profesor, ID_Colegio,Fecha_Contratacion))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f" Profesor ID: {ID_Profesor}, Colegio ID: {ID_Colegio}, insertado correctamente")
        except pyodbc.Error as e:
            print(f"Error al insertar Profesor - Colegio: {e}")
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla Profesor - colegio
    def Eliminar_ProfesorColegio(self, ID_Profesor: int, ID_Colegio: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarProfesorColegio(?, ?)", (ID_Profesor, ID_Colegio))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Profesor - colegio, con ID {ID_Profesor} y {ID_Colegio} eliminado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar Profesor - colegio: {e}")
            
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla Profesor - colegio  
    def Actualizar_ProfesorColegio(self, ID_Profesor : int, ID_Colegio: int, NuevoFecha_Contratacion: datetime) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarProfesorColegio(?, ?, ?)", (ID_Profesor, ID_Colegio, NuevoFecha_Contratacion))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Profesor colegio con ID {ID_Profesor} y {ID_Colegio} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Profesor colegio: {e}")
            
    #14). Call proc Table Curso
    #Llamando al procedimiento almacenado que consulta la tabla Curso
    
    def Seleccionar_Curso(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarCurso()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_Curso = []  
        for elemento in cursor:
            dtCurso = Curso()
            dtCurso.SetID_Curso(elemento[0])
            dtCurso.SetNombre(elemento[1])
            dtCurso.SetNum_Estudiantes(elemento[2])
            dtCurso.SetID_Colegio(elemento[3])
            Datos_Curso.append(dtCurso)
            
        cursor.close()
        conexion.close()

        for dtCurso in Datos_Curso:
            print(f"Curso: {dtCurso.GetID_Curso()} - {dtCurso.GetNombre()} - {dtCurso.GetNum_Estudiantes()} - {dtCurso.GetID_Colegio()}") 
            
    #Llamando al procedimiento almacenado que inserta datos en la tabla Curso
    def Insertar_Curso(self, ID_Curso : int, Nombre: str, Num_Estudiantes: int, ID_Colegio: int) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarCurso(?, ?, ?, ?)", (ID_Curso, Nombre, Num_Estudiantes, ID_Colegio))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f" Curso ID: {ID_Curso}, insertado correctamente")
        except pyodbc.Error as e:
            print(f"Error al insertar Curso: {e}")
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla curso
    def Eliminar_Curso(self, ID_Curso: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarCurso(?)", (ID_Curso))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Curso con ID {ID_Curso} eliminado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar curso: {e}")
            
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla Curso 
    def Actualizar_Curso(self,  ID_Curso : int, NuevoNombre: str,NuevoNum_Estudiantes: int, ID_Colegio: int) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarCurso(?, ?, ?, ?)", (ID_Curso, NuevoNombre, NuevoNum_Estudiantes, ID_Colegio))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Curso con ID {ID_Curso} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Curso: {e}")
            
    
    #15). Call proc Table Asignatura
    #Llamando al procedimiento almacenado que consulta la tabla Asignatura
    
    def Seleccionar_Asignatura(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarAsignatura()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_Asignatura = []  
        for elemento in cursor:
            dtAsignatura = Asignatura()
            dtAsignatura.SetID_Asignatura(elemento[0])
            dtAsignatura.SetNombre(elemento[1])
            dtAsignatura.SetID_Curso(elemento[2])
            Datos_Asignatura.append(dtAsignatura)
            
        cursor.close()
        conexion.close()

        for dtAsignatura in Datos_Asignatura:
            print(f"Asignatura : {dtAsignatura.GetID_Asignatura()} - {dtAsignatura.GetNombre()} - {dtAsignatura.GetID_Curso()}") 
            
    #Llamando al procedimiento almacenado que inserta datos en la tabla Curso
    def Insertar_Asignatura(self, ID_Asignatura : int, Nombre: str, ID_Curso: int) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarAsignatura(?, ?, ?)", (ID_Asignatura, Nombre, ID_Curso))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f" Asignatura con ID: {ID_Curso}, insertado correctamente")
        except pyodbc.Error as e:
            print(f"Error al insertar asignatura: {e}")
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla Asignatura
    def Eliminar_Asignatura(self, ID_Asignatura: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarAsignatura(?)", (ID_Asignatura))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Asignatura con ID {ID_Asignatura}, eliminada correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar asignatura: {e}")
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla Asignatura
    def Actualizar_Asignatura(self, ID_Asignatura : int, NuevoNombre: str, ID_Curso: int) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarAsignatura(?, ?, ?)", (ID_Asignatura, NuevoNombre, ID_Curso))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Asignatura con ID {ID_Asignatura} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Asignatura: {e}")
            
            
    #16). Call proc Table Profesor-Asignatura
    #Llamando al procedimiento almacenado que consulta la tabla Profesor-Asignatura
    
    def Seleccionar_ProfesorAsignatura(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarProfesorAsignatura()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_ProfesorAsignatura = []  
        for elemento in cursor:
            proAsignatura = Profesor_Asignatura()
            proAsignatura.SetID_Profesor(elemento[0])
            proAsignatura.SetID_Asignatura(elemento[1])
            proAsignatura.SetFechaContratacion(elemento[2])
            Datos_ProfesorAsignatura.append(proAsignatura)
            
        cursor.close()
        conexion.close()

        for proAsignatura in Datos_ProfesorAsignatura:
            print(f"Profesor - Asignatura: {proAsignatura.GetID_Profesor()} - {proAsignatura.GetID_Asignatura()} - {proAsignatura.GetFechaContratacion()}") 
            
    #Llamando al procedimiento almacenado que inserta datos en la tabla Profesor - Asignatura
    def Insertar_ProfesorAsignatura(self, ID_Profesor: int, ID_Asignatura: int, Fecha_Contratacion: datetime) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarProfesorAsignatura(?, ?, ?)", (ID_Profesor, ID_Asignatura, Fecha_Contratacion))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f" Profesor_Asignatura con ID: {ID_Profesor} y {ID_Asignatura} , insertado correctamente")
        except pyodbc.Error as e:
            print(f"Error al insertar Profesor_Asignatura: {e}")
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla Profesor - Asignatura
    def Eliminar_ProfesorAsignatura(self, ID_Profesor: int, ID_Asignatura: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarProfesorAsignatura(?, ?)", (ID_Profesor, ID_Asignatura))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Profesor - Asignatura con ID {ID_Profesor} y {ID_Asignatura}, eliminado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar Profesor - Asignatura: {e}")
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla Profesor - Asignatura
    def Actualizar_ProfesorAsignatura(self, ID_Profesor: int, ID_Asignatura: int, NuevoFecha_Contratacion: datetime) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarProfesorAsignatura(?, ?, ?)", (ID_Profesor, ID_Asignatura, NuevoFecha_Contratacion))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Profesor - Asignatura con ID  {ID_Profesor} y {ID_Asignatura} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Profesor - Asignatura: {e}")
            
    #17). Call proc Table Estudiante
    #Llamando al procedimiento almacenado que consulta la tabla Estudiante
    
    def Seleccionar_Estudiante(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarEstudiante()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_Estudiante = []  
        for elemento in cursor:
            dtEstudiante = Estudiante()
            dtEstudiante.SetID_Estudiante(elemento[0])
            dtEstudiante.SetNombre(elemento[1])
            dtEstudiante.SetApellido(elemento[2])
            dtEstudiante.SetFecha_Nacimiento(elemento[3])
            dtEstudiante.SetID_Colegio(elemento[4])
            Datos_Estudiante.append(dtEstudiante)
            
        cursor.close()
        conexion.close()

        for dtEstudiante in Datos_Estudiante:
            print(f" Estudiante: {dtEstudiante.GetID_Estudiante()}- {dtEstudiante.GetNombre()} - {dtEstudiante.GetApellido()} - {dtEstudiante.GetFecha_Nacimiento()} - {dtEstudiante.GetID_Colegio()}") 
     
    #Llamando al procedimiento almacenado que inserta datos en la tabla Estudiante
    def Insertar_Estudiante(self, ID_Estudiante : int, Nombre: str, Apellido: str, Fecha_Nacimiento: datetime, ID_Colegio: int) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarEstudiante(?, ?, ?, ?, ?)", (ID_Estudiante, Nombre, Apellido, Fecha_Nacimiento, ID_Colegio))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f" Estudiante : {Nombre}, con ID: {ID_Estudiante}, insertado correctamente")
        except pyodbc.Error as e:
            print(f"Error al insertar Estudiante: {e}") 
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla Estudiante
    def Eliminar_Estudiante(self, ID_Estudiante: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarEstudiante(?)", (ID_Estudiante))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Estudiante con ID {ID_Estudiante}, eliminado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar Estudiante: {e}")
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla Estudiante
    def Actualizar_Estudiante(self, ID_Estudiante : int, NuevoNombre: str, NuevoApellido: str, NuevoFecha_Nacimiento: datetime, ID_Colegio: int) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarEstudiante(?, ?, ?, ?, ?)", (ID_Estudiante, NuevoNombre, NuevoApellido, NuevoFecha_Nacimiento, ID_Colegio))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Estudiante con ID  {ID_Estudiante}, actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Estudiante: {e}")
            
    #18). Call proc Table Estudiante-Asignatura
    #Llamando al procedimiento almacenado que consulta la tabla Estudiante-Asignatura
    
    def Seleccionar_EstudianteAsignatura(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        consulta: str = "{CALL SeleccionarEstudianteAsignatura()}"  
        cursor = conexion.cursor()
        cursor.execute(consulta)
  
        Datos_EstudianteAsignatura = []  
        for elemento in cursor:
            EstAsignatura = Estudiante_Asignatura()
            EstAsignatura.SetID_Estudiante(elemento[0])
            EstAsignatura.SetID_Asignatura(elemento[1])
            EstAsignatura.SetFecha_matricula(elemento[2])
            Datos_EstudianteAsignatura.append(EstAsignatura)
            
        cursor.close()
        conexion.close()

        for EstAsignatura in Datos_EstudianteAsignatura:
            print(f"Estudiante - Asignatura: {EstAsignatura.GetID_Estudiante()} - {EstAsignatura.GetID_Asignatura()} - {EstAsignatura.GetFecha_matricula()}") 
            
    #Llamando al procedimiento almacenado que inserta datos en la tabla Estudiante - Asignatura
    def Insertar_EstudianteAsignatura(self, ID_Estudiante: int, ID_Asignatura: int, Fecha_matricula: datetime) -> None:
        try:
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor() 
            cursor.execute("CALL InsertarEstudianteAsignatura(?, ?, ?)", (ID_Estudiante, ID_Asignatura, Fecha_matricula))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f" Estudiante_Asignatura con ID: {ID_Estudiante}, insertado correctamente")
        except pyodbc.Error as e:
            print(f"Error al insertar Estudiante_Asignatura: {e}")
            
    #Llamando al procedimiento almacenado que Elimina datos en la tabla Estudiante - Asignatura
    def Eliminar_EstudianteAsignatura(self, ID_Estudiante: int, ID_Asignatura: int) -> None:
        try:    
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL EliminarEstudianteAsignatura(?, ?)", (ID_Estudiante, ID_Asignatura ))
            conexion.commit()  
            cursor.close()
            conexion.close()
            print(f"Estudiante - Asignatura con ID {ID_Estudiante} y {ID_Asignatura} , eliminado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al eliminar Estudiante - Asignatura: {e}")
            
    #Llamando al procedimiento almacenado que actualiza datos en la tabla Estudiante - Asignatura
    def Actualizar_EstudianteAsignatura(self, ID_Estudiante: int, ID_Asignatura: int, NuevoFecha_matricula: datetime) -> None:
        try: 
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()
            cursor.execute("CALL ActualizarEstudianteAsignatura(?, ?, ?)", (ID_Estudiante, ID_Asignatura, NuevoFecha_matricula))
            conexion.commit()  
            cursor.close()
            conexion.close()   
            print(f"Estudiante - Asignatura con ID  {ID_Estudiante} y {ID_Asignatura} actualizado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al actualizar Estudiante - Asignatura: {e}")
                        
conexion: Conexion = Conexion()
#1) ----Invocando Funciones Departamento

#conexion.SeleccionarDepartamento()
#conexion.Eliminar_Departamento(1)
#conexion.Insertar_Departamento(7, 'Tolima')
#conexion.Actualizar_Departamento(2, 'Guajira')

#2) ----Invocando Funciones SecEducacion_Departamental

#conexion.Seleccionar_SecEducacion_Departamental()
#conexion.Insertar_SecEducacion_Departamental( 7, 'Secretaría Tunja','calle 27 # 16 - 25', 'secTunja@gmail.com', 7)
#conexion.Eliminar_SecEducacion_Departamental(3)
#conexion.Actualizar_SecEducacion_Departamental(4, 'Secreatria Chocó', 'calle 72 # 87 - 58', 'secChoco@gmail.com', 4)

#3) ----Invocando Funciones DirSecretaria_Educacion

#conexion.Seleccionar_DirSecretaria_Educacion()
#conexion.Insertar_DirSecEducacion_Departamental(7, 'Juan Andrés', 'Arreaga', 'Masculino', 'juanarreaga@gmail.com', 'Carrera 57 sur # 48 - 76', '2022-01-20', '1987-03- 15', 2 ) 
#conexion.Eliminar_DirSecEducacion_Departamental(4)
#conexion.Actualizar_DirSecEducacion_Departamental(3, 'David', 'Gonzáles', 'Masculino', 'davidgonzales@gmail.com', 'av 78 # 25 - 36', '2023-07-22', '1980-04-03', 2)

#4) ----Invocando Funciones Regional

#conexion.Seleccionar_Regional()
#conexion.Insertar_Regional(6, 'Guajira', 6)
#conexion.Eliminar_Regional(4)
#conexion.Actualizar_Regional(3, 'Chocó', 5)

#5) ----Invocando Funciones DirRegional

#conexion.Seleccionar_DirRegional()
#conexion.Insertar_DirRegional(7, 'Salomon', 'Gutierrez', 'Masculino', 'salomongut@gmail.com', 'av 90 # 23 - 16', '2021-02-16', '1976-02-11', 4)
#conexion.Eliminar_DirRegional(1)
#conexion.Actualizar_DirRegional(3, 'Gabriela', 'Tafur', 'Femenino', 'gabrielaT@gmail.com', 'Carrera 54 # 87 - 26', '2024-05-02', '1977-06-06', 4)

#6) ----Invocando Funciones Ciudad

#conexion.Seleccionar_Ciudad()
#conexion.Insertar_Ciudad(7, 'Yopal', 2)
#conexion.Eliminar_Ciudad(2)
#conexion.Actualizar_Ciudad(4, 'Villavicencio', 5)

#7) ----Invocando Funciones Comuna

#conexion.Seleccionar_Comuna()
#conexion.Insertar_Comuna(6, 'Comuna 6', 2)
#conexion.Eliminar_Comuna(2)
#conexion.Actualizar_Comuna(3, 'Comuna 7', 3)

#8) ----Invocando Funciones director Comuna

#conexion.Seleccionar_DirComuna()
#conexion.Insertar_DirectorComuna(7, 'Alejandra', 'Martínez', 'Femenino', 'aleja@gmail.com', 'calle 46 # 89 - 28', '2024-01-07', '1967-07-16', 3)
#conexion.Eliminar_DirectorComuna(7)
#conexion.Actualizar_DirComuna(3, 'Jorge', 'Pérez', 'Masculino', 'jprge@hotmail.com', 'av 90 # 23', '2024-03-21', '2000-02-012', 3)

#9) ----Invocando Funciones Colegio

#conexion.Seleccionar_Colegio()
#conexion.Insertar_Colegio(6,'Colegio F', 'av 65 # 87' , '4536789', 2)
#conexion.Eliminar_Colegio(6)
#conexion.Actualizar_Colegio(3, 'Colegio B', 'Calle 34 # 5 - 16', '3245687', 3)

#10) ----Invocando Funciones Rector

#conexion.Seleccionar_Rector()
#conexion.Insertar_Rector(6, 'Mauricio', 'Arango', 'Masculino', 'mauroara@gmail.com', 'cra 27 # 87 - 16', '2024-03-212', '2001-02-01', 5)
#conexion.Eliminar_Rector(6)
#conexion.Actualizar_Rector(6, 'María', 'Garza', 'Femenino', 'garzamaria@gmail.com', 'carr 23 # 28 - 18', '2022-01-21', '1997-05-025', 2)

#11) ----Invocando Funciones Secretaria_Colegio

#conexion.Seleccionar_SecretariaColegio()
#conexion.Insertar_SecretariaColegio(6, 'Juanita', 'Pérez', 'Femenino', 'perezjuanita@gmail.com', 'carrera 23 # 67 - 21', '2021-05-23', '1990-02-05', 2)
#conexion.Eliminar_SecretariaColegio(6)
#conexion.Actualizar_SecretariaColegio(6, 'Carmela', 'Giraldo', 'Femenino', 'carmelita@gmail.com', 'calle 34 # 76 - 26', '2020-05-23', '1991-02-05', 2)

#12) ----Invocando Funciones Profesor

#conexion.Seleccionar_Profesor()
#conexion.Insertar_Profesor(9, 'Nadia', 'Urango', 'Femenino', 'nadia@gmail.com', 'carrera 34 # 67 - 28', '1990-03-21', 'Ingeniera en sistemas', 3)
#conexion.Eliminar_Profesor(9)
#conexion.Actualizar_Profesor(9, 'Juan', 'Barrios', 'Masculino', 'juanb@gmail.com', 'calle 76 # 28 - 12', '1998-07-25', 'Ingeniera en sistemas', 3 )

#13 ----Invocando Funciones Profesor - Colegio

#conexion.Seleccionar_ProfesorColegio()
#conexion.Insertar_ProfesorColegio(7, 2,'2021-07-05')
#conexion.Eliminar_ProfesorColegio(5, 5)
#conexion.Actualizar_ProfesorColegio(5, 5, '2023-04-10' )

#14 ----Invocando Funciones Curso

#conexion.Seleccionar_Curso()
#conexion.Insertar_Curso(6, 'Octavo', 40, 2)
#conexion.Eliminar_Curso(6)
#conexion.Actualizar_Curso(6, 'Once', 35, 2)


#15 ----Invocando Funciones Asignatura

#conexion.Seleccionar_Asignatura()
#conexion.Insertar_Asignatura(6, 'Informática', 3)
#conexion.Eliminar_Asignatura(6)
#conexion.Actualizar_Asignatura(6, 'DB', 3)

#16 ----Invocando Funciones profesorAsignatura

#conexion.Seleccionar_ProfesorAsignatura()
#conexion.Insertar_ProfesorAsignatura(1, 3,'2019-08-05')
#conexion.Eliminar_ProfesorAsignatura(5, 5)
#conexion.Actualizar_ProfesorAsignatura(5, 5, '2020-10-05')

#17 ----Invocando Funciones Estudiante

#conexion.Seleccionar_Estudiante()
#conexion.Insertar_Estudiante(6, 'Esther', 'Garzón', '2021-10-09', 2)
#conexion.Eliminar_Estudiante(6)
#conexion.Actualizar_Estudiante(6, 'Jaime', 'Garza', '2021-10-09', 2 )

#18 ----Invocando Funciones Estudiante- Asignatura

#conexion.Seleccionar_EstudianteAsignatura()
#conexion.Insertar_EstudianteAsignatura(6, 6, '2024-01-09')
#conexion.Eliminar_EstudianteAsignatura(5, 5)
#conexion.Actualizar_EstudianteAsignatura(6, 6, '2023-02-05')



