from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api_v1.endpoints.users import fastapi_users
from app.db.session import get_async_session
from app.schemas.posts import PostRead, PostCreate

router = APIRouter()

current_active_user = fastapi_users.current_user(active=True)

posts = [
    {'title': "title1", 'text': 'text1', 'created': datetime(2001, 2, 2), 'user_id': '123'},
    {'title': "title2", 'text': 'text2', 'created': datetime(2001, 2, 2), 'user_id': '123'},
    {'title': "title3", 'text': 'text3', 'created': datetime(2001, 2, 2), 'user_id': '123'},
    {'title': "title4", 'text': 'text4', 'created': datetime(2001, 2, 2), 'user_id': '123'},
    {'title': "title5", 'text': 'text5', 'created': datetime(2001, 2, 2), 'user_id': '123'},
    {'title': "title6", 'text': 'text6', 'created': datetime(2001, 2, 2), 'user_id': '123'},
]


@router.post('/create', response_model=PostRead)
async def create_post(post: PostCreate,
                      db: AsyncSession = Depends(get_async_session),
                      current_user=Depends(current_active_user)):
    print(post)
    print(current_user)
    return PostRead(title=post.title, text=post.text, created=datetime(2001, 1, 1), user_id='123')


@router.get('/', response_model=List[PostRead])
async def read_posts(current_user=Depends(current_active_user)):
    return [PostRead(**post) for post in posts]
