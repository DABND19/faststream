import pytest

from faststream.redis import TestRedisBroker


@pytest.mark.asyncio
async def test_stream_pub():
    from docs.docs_src.redis.stream.pub import broker, on_input_data

    publisher = list(broker._publishers)[0]  # noqa: RUF015

    async with TestRedisBroker(broker) as br:
        await br.publish({"data": 1.0}, stream="input-stream")
        on_input_data.mock.assert_called_once_with({"data": 1.0})
        publisher.mock.assert_called_once_with({"data": 2.0})
