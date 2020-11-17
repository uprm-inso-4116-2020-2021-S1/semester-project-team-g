from cth import db
from sqlalchemy.ext.automap import automap_base

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Institution = Base.classes.institutions
Operator = Base.classes.operator
Citizen = Base.classes.citizen
Test = Base.classes.tests
Infected = Base.classes.infected
Recovered = Base.classes.recovered
Illness = Base.classes.illness