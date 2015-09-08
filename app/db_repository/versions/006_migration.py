from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
link = Table('link', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=255)),
    Column('url', String(length=255)),
    Column('category', String(length=64)),
    Column('order', Integer),
    Column('cac_required', Boolean),
    Column('login_required', Boolean),
    Column('gov_only', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['link'].columns['gov_only'].create()
    post_meta.tables['link'].columns['login_required'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['link'].columns['gov_only'].drop()
    post_meta.tables['link'].columns['login_required'].drop()
