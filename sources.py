#!/usr/bin/env python

from buildbot.plugins import changes

sources = []
sources.append(changes.GitHubPullrequestPoller(
    owner='aliceinwire',
    branches=None,
    repo='linux-patches'))

sources.append(changes.GitHubPullrequestPoller(
    owner='gentoo',
    branches=None,
    category='gentoo-pull',
    repo='gentoo'))

sources.append(changes.GitPoller(
    repourl='https://github.com/gentoo/gentoo.git',
    branches=True,
    category="gentoo-pull",
    pollinterval=10))

sources.append(changes.GitPoller(
    repourl='https://github.com/aliceinwire/linux-patches',
    only_tags=True,
    category="gentoo-tags-git",
    pollinterval=300))

sources.append(changes.GitPoller(
    repourl='https://github.com/aliceinwire/linux-patches',
    branches=True,
    category="gentoo-git",
    pollinterval=300))

