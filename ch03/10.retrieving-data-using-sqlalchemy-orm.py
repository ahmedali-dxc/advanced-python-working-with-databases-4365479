from sqlalchemy import Column, String, Integer, create_engine, ForeignKey, Select, result_tuple
from sqlalchemy.orm import registry, relationship, Session

# Create the engine
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/projects', echo=True)

mapper_registry = registry()

Base = mapper_registry.generate_base()

class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=50))

    def __repr__(self):
        return "<Project(title='{0}', description='{1}')>".format(self.title, self.description)

class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    description = Column(String(length=50))

    project = relationship("Project")

    def __repr__(self):
        return "<Task(description='{0}')>".format(self.description)

Base.metadata.create_all(engine)

with Session(engine) as session:
    stm = Select(Project).where(Project.title == 'Organize closet')
    results = session.execute(stm)
    organize_closet_project = results.scalar() # return 1st row

    stm = Select(Task).where(Task.project_id == organize_closet_project.project_id)
    results = session.execute(stm)
    for task in results:
        print(task)