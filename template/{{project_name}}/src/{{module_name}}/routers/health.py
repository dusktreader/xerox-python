from fastapi import APIRouter, Response
from fastapi import status

router = APIRouter(prefix="/health")


@router.get(
    "",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={204: {"description": "API is healthy"}},
)
async def fetch_health():
    return Response(status_code=status.HTTP_204_NO_CONTENT)
