"""
generic foriegn key:
- generic foriegn key is used to give a foriegn key relationship for a model to other model as we like
- it contains 
    content_type: where foriegn key is initiated 
    object_id: id of instance of the model being linked to 
    content_object : combines content type and object id , query is initiated to get instance of foriegn model

generic relation:
- generic relation is used to get the instance of model with which it is linked with

example-
- models - teacher,course,material
- few instances in course must be linked to material or a teacher
- the generic foriegn key is used in course so that it can be connected to eithe teacher or material
- generic relation is used for teacher and material so that a a instance of these and find out to which instance in course it is linked with.