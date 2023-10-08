from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_post(user):
    query = (
        """
        mutation {
            addPost(postData: {
                userId: %s,
                title: "My Test Title",
                body: "Body content",
            })
            {
                id
                userId
                title
                body
                comments {
                  id
                }
            }
        }
    """
        % user.id
    )

    response = client.post("/graphql", json={"query": query})
    assert response is not None
    assert response.status_code == 200

    result = response.json()
    assert result["data"]["addPost"]["userId"] == user.id
    assert result["data"]["addPost"]["title"] == "My Test Title"
    assert result["data"]["addPost"]["body"] == "Body content"
    assert result["data"]["addPost"]["comments"] == []
