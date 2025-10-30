from typing import Any, Dict, List, Optional
from urllib.parse import urlencode

import requests


class OpenLibraryAPI:
    """Client for the Open Library Search API"""

    def __init__(self, string: Optional[str] = "search"):
        self.string = string
        self.BASE_URL = f"https://openlibrary.org/{self.string}.json"

    def search_books(
        self,
        query: Optional[str] = None,
        title: Optional[str] = None,
        author: Optional[str] = None,
        fields: Optional[List[str]] = None,
        sort: Optional[str] = None,
        lang: Optional[str] = None,
        limit: int = 10,
        page: int = 1,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Search for books using the Open Library API

        Args:
            query: General search query
            title: Search by title
            author: Search by author
            fields: List of fields to return (use '*' for all, 'availability' for availability data)
            sort: Sort results (e.g., 'new', 'old', 'random', 'rating')
            lang: Two-letter language code (ISO 639-1)
            limit: Number of results per page
            page: Page number (starts at 1)
            offset: Alternative to page for pagination

        Returns:
            Dictionary containing search results
        """
        params = {}

        # Add search parameters
        if query:
            params["q"] = query
        if title:
            params["title"] = title
        if author:
            params["author"] = author
        if fields:
            params["fields"] = ",".join(fields)
        if sort:
            params["sort"] = sort
        if lang:
            params["lang"] = lang
        if limit:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        else:
            params["page"] = page

        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return {}


# Example usage
def main():
    api = OpenLibraryAPI("search")

    # Example 1: Simple search
    print("=== Simple Search ===")
    results = api.search_books(query="the lord of the rings", limit=1)
    print(results)


if __name__ == "__main__":
    main()
