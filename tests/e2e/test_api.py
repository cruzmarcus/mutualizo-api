import httpx
from fastapi import status


class TestPingEndpoint:
    async def test_ping_ok(self, client: httpx.AsyncClient, settings) -> None:
        response = await client.get("/v1/ping")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["name"] == settings.API_TITTLE


class TestReverseIntegersEndpoint:
    async def test_get_reverse_integers_ok(
        self, client: httpx.AsyncClient
    ) -> None:
        parameters = {"number": -123}

        response = await client.get("v1/reverse-integers", params=parameters)

        assert response.status_code == status.HTTP_200_OK

    async def test_get_reverse_integers_wrong_uri_redirect(
        self, client: httpx.AsyncClient
    ) -> None:
        parameters = {"number": 300}

        response = await client.get("v1/reverse-integers/", params=parameters)

        assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT

    async def test_get_reverse_integers_unprocessable_entity(
        self, client: httpx.AsyncClient
    ) -> None:
        invalid_parameters = {"sentences": -0.92}

        response = await client.get(
            "v1/average-words-length", params=invalid_parameters
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


class TestAverageWordsLengthEndpoint:
    async def test_get_average_words_length_ok(
        self, client: httpx.AsyncClient
    ) -> None:
        parameters = {
            "sentence": "Hi all, my name is Tom... I am originally from Brazil."
        }

        response = await client.get(
            "v1/average-words-length", params=parameters
        )

        assert response.status_code == status.HTTP_200_OK

    async def test_get_average_words_length_wrong_uri_redirect(
        self, client: httpx.AsyncClient
    ) -> None:
        parameters = {
            "sentence": "Hi all, my name is Tom... I am originally from Brazil."
        }

        response = await client.get(
            "v1/average-words-length/", params=parameters
        )

        assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT

    async def test_get_average_words_length_unprocessable_entity(
        self, client: httpx.AsyncClient
    ) -> None:
        invalid_parameters = {
            "sentences": "Hi all, my name is Tom... I am originally from Brazil."
        }

        response = await client.get(
            "v1/average-words-length", params=invalid_parameters
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


class TestMatchedAndMisMatchedWordsEndpoint:
    async def test_get_matched_and_mismatched_words_ok(
        self, client: httpx.AsyncClient
    ) -> None:
        parameters = {
            "sentence_one": "We are really pleased to meet you in our city",
            "sentence_two": "The city was hit by a really heavy storm",
        }

        response = await client.get(
            "v1/matched-and-mismatched-words", params=parameters
        )

        assert response.status_code == status.HTTP_200_OK

    async def test_get_matched_and_mismatched_words_wrong_uri_redirect(
        self, client: httpx.AsyncClient
    ) -> None:
        parameters = {
            "sentence_one": "We are really pleased to meet you in our city",
            "sentence_two": "The city was hit by a really heavy storm",
        }

        response = await client.get(
            "v1/matched-and-mismatched-words/", params=parameters
        )

        assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT

    async def test_get_matched_and_mismatched_words_unprocessable_entity(
        self, client: httpx.AsyncClient
    ) -> None:
        invalid_parameters = {
            "sentence_1": "We are really pleased to meet you in our city",
            "sentence_2": "The city was hit by a really heavy storm",
        }

        response = await client.get(
            "v1/matched-and-mismatched-words", params=invalid_parameters
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
