MIXED_TEST_DISCOVERY_SOURCE = '''def test_sync():
    """Synchronous test."""
    pass

async def test_async():
    """Asynchronous test."""
    pass

@pytest.mark.asyncio
async def test_decorated_async():
    pass

async def async_helper():
    pass

class TestAsyncCases:
    async def test_async_method(self):
        """Asynchronous method."""
        pass

    async def method_helper(self):
        pass
'''
