#    Copyright (C) Midhun KM 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from sqlalchemy import Column, String, UnicodeText

from fridaybot.modules.sql_helper import BASE, SESSION


class Anp(BASE):
    __tablename__ = "anp"
    amazon_url = Column(UnicodeText, primary_key=True)
    budget = Column(String(14))

    def __init__(self, budget, amazon_url):
        self.budget = budget
        self.amazon_url = amazon_url


Anp.__table__.create(checkfirst=True)


def add_new_tracker(budget: int, amazon_url):
    tracker_adder = Anp(str(budget), amazon_url)
    SESSION.add(tracker_adder)
    SESSION.commit()


def get_tracker_info(amazon_url: str):
    try:
        s__ = SESSION.query(Anp).get(str(amazon_url))
        return int(s__.budget), s__.amazon_url
    finally:
        SESSION.close()
        
def is_tracker_in_db(amazon_url: str):
    try:
        s__ = SESSION.query(Anp).get(str(amazon_url))
        return int(s__.budget)
    finally:
        SESSION.close()
        
        
def get_all_tracker():
    stark = SESSION.query(Anp).all()
    SESSION.close()
    return stark


def rm_tracker(amazon_url: str):
    warner = SESSION.query(Anp).get(str(amazon_url))
    if warner:
        SESSION.delete(warner)
        SESSION.commit()
