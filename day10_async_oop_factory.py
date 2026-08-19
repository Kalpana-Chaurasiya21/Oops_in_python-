# Async OOP & Factory Pattern
# Standard __init__ constructors in Python CANNOT be declared async.
# To safely initialize objects requiring asynchronous I/O (e.g., opening database pools,
# making network requests), we use async static factory methods.

import asyncio


class DatabaseService:
    """Class representing a non-blocking database connection pool."""

    def __init__(self, connection_string: str, pool_size: int):
        # Private constructor logic—holds synchronous state variables
        self.connection_string = connection_string
        self.pool_size = pool_size
        self._is_connected = False

    @classmethod
    async def create(cls, connection_string: str, pool_size: int = 5):
        """
        Async Factory Method: Safely handles asynchronous setup 
        before returning a fully initialized instance.
        """
        instance = cls(connection_string, pool_size)
        await instance._initialize_pool()
        return instance

    async def _initialize_pool(self):
        """Simulates non-blocking connection pool setup."""
        print(f"[Async DB] Connecting to '{self.connection_string}'...")
        await asyncio.sleep(1.0)  # Simulates I/O network delay
        self._is_connected = True
        print(f"[Async DB] Connected successfully with pool size of {self.pool_size}.")

    async def fetch_record(self, record_id: int) -> dict:
        """Asynchronous data fetch method."""
        if not self._is_connected:
            raise RuntimeError("Database connection pool is not initialized!")
        
        print(f"[Async DB] Fetching record ID #{record_id}...")
        await asyncio.sleep(0.5)  # Simulates query execution time
        return {"id": record_id, "status": "active", "data": "Sample Payload"}


#  Example Async Execution 

async def main():
    print("# --- Async OOP Factory Demonstration ---")
    
    # Safe async instantiation via Factory Method
    db = await DatabaseService.create("postgresql://admin:secret@localhost:5432/production_db")
    
    # Executing concurrent non-blocking queries
    results = await asyncio.gather(
        db.fetch_record(101),
        db.fetch_record(102),
        db.fetch_record(103)
    )
    
    print("\nFetch Results:")
    for res in results:
        print(f"- {res}")


if __name__ == "__main__":
    asyncio.run(main())