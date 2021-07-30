class ScopeBuilder:

    #region Public Methods
    def build(self):
        scope = ""
        scope += "user-library-read "
        scope += "user-read-recently-played "
        scope += "user-top-read "
        return scope.rstrip()
