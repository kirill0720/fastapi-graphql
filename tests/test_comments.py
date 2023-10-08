from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_comment(user, post):
    query = """
        mutation {
                    addComment(commentData: {
                        userId: %s,
                        postId: %s,
                        body: "Comment body",
                    })
                    {
                        id
                        userId
                        postId
                        body
                    }
                }
    """ % (
        user.id,
        post.id,
    )

    response = client.post("/graphql", json={"query": query})
    assert response is not None
    assert response.status_code == 200

    result = response.json()
    assert result["data"]["addComment"]["userId"] == user.id
    assert result["data"]["addComment"]["postId"] == post.id
    assert result["data"]["addComment"]["body"] == "Comment body"
