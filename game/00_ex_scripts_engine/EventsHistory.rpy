init -500 python:
    class EventsHistoryRecord( store.object ):
        def __init__( self ):
            self.mName = None
            self.mDay = None

        @classmethod
        def create( cls, aEventName, aFinishDay ):
            record = cls()
            record.mName = aEventName
            record.mDay = aFinishDay
            return record

    class EventsHistory( store.object ):

        def __init__( self ):
            self.mHistory = []


        def record( self, aEventName, aFinishDay ):
            self.mHistory.insert( 0, EventsHistoryRecord.create( aEventName, aFinishDay ) )

        def getDaysSinceLast( self, aCurDay ):
            lastEvent = self.mHistory[0]
            return aCurDay - lastEvent.mDay

        def getDaysSinceEvent( self, aCurDay, aEventName ):
            for event in self.mHistory:
                if event.mName == aEventName:
                    return aCurDay - event.mDay
            return None