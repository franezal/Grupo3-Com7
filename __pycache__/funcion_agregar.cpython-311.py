�
    �gd�  �                   �   � d Z d� ZdS )u�   
Función agregar, sólo sirve para el desafío 4: La Inmobiliaria.
Sólo agrega el inmueble si cumple con las las reglas de validación,
de lo contrario devuelve False y un aviso.
c                  ��  � t          d�  �         i } t          d�  �        | d<   t          d�  �        | d<   t          d�  �        | d<   t          t          d�  �        �  �        | d	<   t          d
�  �        | d<   t          d�  �        | d<   | d         dv rW| d         dv rMt          | d         �  �        dk    r4t          | d         �  �        dk    rt          | d         �  �        dk    r| S t          d�  �         dS )Nz Inserte los datos del inmueble: u   Año: u   añozMetros: �metroszHabitaciones: �habitacioneszGarage: �garagezZona: �zonazEstado: �estado)�A�B�C)�
Disponible�	Reservado�Vendidoi�  �<   �   u4   El inmueble no cumple con las reglas de validación.F)�print�input�bool�int)�inmuebles    �>c:\Users\Usuario\Desktop\Python\Grupo3-Com7\funcion_agregar.py�agregarr      s  � �	�
,�-�-�-��H��X���H�V���z�*�*�H�X��$�%5�6�6�H�^���e�J�/�/�0�0�H�X���X���H�V���z�*�*�H�X�����O�+�+����D�D�D��H�V�����%�%�#�h�x�.@�*A�*A�R�*G�*G��H�^�$�%�%��*�*����D�E�E�E��u�    N)�__doc__r   � r   r   �<module>r      s(   ��� �
� � � � r   