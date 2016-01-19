class Source(object):

  def __init__(self, name):
    self._name = name;

  def __repr__(self):
      return "Source [name: {0}]".format(str(self._name))


class BookSource(Source):

  def __init__(self, book_name, page):
    super(BookSource, self).__init__(book_name)
    self._page = page

  def __repr__(self):
      return "BookSource [name: {0}, page: {1}]".format(str(self._name), str(self._page))


class Comments(object):
  
  # have_made: bool, true if I've made it before
  # stars: int, 1-5
  # notes: string, any notes I have on it, regardless of whether I've made it or not
  # to_improve: string, things I could improve upon
  def __init__(self, have_made, stars, notes, to_improve):
    self._have_made = have_made
    self._stars = stars
    self._notes = notes
    self._to_improve = to_improve

  def __repr__(self):
    return "Comments [have_made: {0}, stars: {1}, notes: {2}, to_improve: {3}]".format(str(self._have_made), str(self._stars), str(self._notes), str(self._to_improve))


class Recipe(object):

  def __init__(self, name, source, ingredients, comments):
    self._name = name
    self._source = source
    self._ingredients = ingredients
    self._comments = comments

  def __repr__(self):
      return "\n* Recipe [name: {0}, source: {1}, ingredients: {2}, comments: {3}]".format(str(self._name), str(self._source), str(self._ingredients), str(self._comments))

