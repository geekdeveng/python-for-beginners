"""
-author : geekdev
-desc : db libarary
"""

from typing import (
    Dict,
    Any
)
from sqlalchemy import (
    create_engine,
    Engine,
    Column, 
    Integer,
    DateTime
)
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    sessionmaker,
    Query, 
    Session
)
from sqlalchemy.dialects.postgresql import JSON

from utils.utils import logger
    
Base = declarative_base()


class Test(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True)
    json_field = Column(JSON, nullable=False)
    time_stamp = Column(DateTime(timezone=True), server_default=func.current_timestamp())
    

class BaseDbWrapper:
    """
    Base wrapper for DB adapter.
    A base class that serves to eliminate source code duplication using sqlalchemy, 
    a general-purpose database framework.
    It is based on the environment created in postgresql.sql.
    """

    def __init__(self, config: Dict) -> None:
        """
        -desc           : __init__ function.
        -param config   : config object with db connection information.
                          Information in db_info.json.
        -return         : None
        """
        
        DB_URL = f"{config['db_kind']}://{config['user']}:{config['pwd']}@{config['host']}:{config['port']}/{config['db_name']}" 
        
        # Managed as connection pool by setting pool_size among create_engine() arg.
        self.__engine: Engine = create_engine(
            DB_URL, 
            pool_pre_ping=True, 
            pool_size=8, 
            max_overflow=0
        )
        
        Base.metadata.create_all(self.__engine)
        self._session: Session = self.__make_session() # protected
        
    def __del__(self) -> None:
        """
        -desc           : __del__ function.
        -param config   : None
        -return         : None
        """
        
        # When the object is destroyed, all sessions are terminated.
        self._session.close_all()
    
    def __make_session(self) -> Session:
        """
        -desc           : make a Session object.
        -param config   : None
        -return         : Session
        """
        
        Session_: sessionmaker[Session] = sessionmaker(bind = self.__engine)
        session: Session = Session_()
        
        return session


class DbWrapper(BaseDbWrapper):
    """
    A wrapper for DB adapter.
    """
    
    def __init__(self, config: Dict) -> None:
        """
        -desc           : init function.
        -param config   : config object with db connection information.
        -return         : None
        """
        
        super().__init__(config)

    def __del__(self) -> None:
        """
        -desc           : __del__ function.
        -param config   : None
        -return         : None
        """
        
        super().__del__()

    #####################################################
    # orm query
    async def insert_to_test_tbl(self, json_obj: Any) -> None:
        """
        -desc           : insert to test table.
        -param json_obj : json object
        -return         : None
        """
        
        try:
            test: Test = Test(json_field = json_obj)
            self._session.add(test)
            self._session.commit() # Return to pool with commit
        except Exception as e:
            self._session.rollback() # Return to pool with rollback
            logger.error(e)
            
    async def select_latest_from_test_tbl(self) -> Test:
        """
        -desc           : select latest row from test table.
                          First of all, it is set to import only the latest one data here.
        -param json_obj : None
        -return         : class Test(1 row in postgresql table)
        """
        
        try:
            rows: Query[Test] = self._session.query(Test).order_by(Test.time_stamp.desc()).limit(1)
            row:Test = rows.one()
        except Exception as e:
            logger.error(e)
            
        return row