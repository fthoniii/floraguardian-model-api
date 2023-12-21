eval 'set +o history' 2>/dev/null || setopt HIST_IGNORE_SPACE 2>/dev/null
 touch ~/.gitcookies
 chmod 0600 ~/.gitcookies

 git config --global http.cookiefile ~/.gitcookies

 tr , \\t <<\__END__ >>~/.gitcookies
source.developers.google.com,FALSE,/,TRUE,2147483647,o,git-c006bsy3675.bangkit.academy=1//0guVvU_BWbvwCCgYIARAAGBASNwF-L9IrHQ_N-FoFdT7z1qRWYiZ-p7STUpLymR8DzaZUxn6ZmMnXIKmeve8jmp8nPWHt4ezEZBc
__END__
eval 'set -o history' 2>/dev/null || unsetopt HIST_IGNORE_SPACE 2>/dev/null
