# Changelog

## 0.6.0 (2025-12-18)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/meta-llama/llama-api-python/compare/v0.5.0...v0.6.0)

### Features

* **api:** manual updates ([345a9f0](https://github.com/meta-llama/llama-api-python/commit/345a9f0554fe30991f936078a3242e44c0cca302))
* **api:** manual updates ([a87c139](https://github.com/meta-llama/llama-api-python/commit/a87c139abe8dc412688855d2ea8226e02d3d1376))
* **api:** manual updates ([2f2aed5](https://github.com/meta-llama/llama-api-python/commit/2f2aed50d52ca6d1e23523a6d4a2469445feb088))


### Bug Fixes

* **client:** close streams without requiring full consumption ([cb29768](https://github.com/meta-llama/llama-api-python/commit/cb29768aa1a4c3d9e8e94ef28cfa40a856618fb4))
* compat with Python 3.14 ([009ca0d](https://github.com/meta-llama/llama-api-python/commit/009ca0d914ec813285e1f195d645871f9cd3d6df))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([eb03850](https://github.com/meta-llama/llama-api-python/commit/eb03850c5905d443da89b71fe8306af8cf5d7062))
* ensure streams are always closed ([4b8f9b7](https://github.com/meta-llama/llama-api-python/commit/4b8f9b7b7f63e0d72daf9bd24c3f12c424040c6d))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([aab06ad](https://github.com/meta-llama/llama-api-python/commit/aab06adc22ed41bd16af636c3bc94e08b9bf2c82))
* use async_to_httpx_files in patch method ([7a5d301](https://github.com/meta-llama/llama-api-python/commit/7a5d3019d53edd2a3b92c8aa91971aa3421ae758))


### Chores

* add missing docstrings ([edaf4a2](https://github.com/meta-llama/llama-api-python/commit/edaf4a2677b2c2a5d4b89a96ac1de289430c6957))
* bump `httpx-aiohttp` version to 0.1.9 ([29874b0](https://github.com/meta-llama/llama-api-python/commit/29874b0abe332ac6c10d44fa93088bd13a4b793f))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([8c1ce31](https://github.com/meta-llama/llama-api-python/commit/8c1ce316a22980fd33b11bacb6f23d3166322f13))
* **docs:** use environment variables for authentication in code snippets ([e04fade](https://github.com/meta-llama/llama-api-python/commit/e04fade6f4b6c8ce315e337a7f58b7b72a981a28))
* **internal/tests:** avoid race condition with implicit client cleanup ([1b7f280](https://github.com/meta-llama/llama-api-python/commit/1b7f2809275a7c39377d5841dd77e52bad1476ed))
* **internal:** add missing files argument to base client ([9223e75](https://github.com/meta-llama/llama-api-python/commit/9223e753f32938fc39e0866ce8f86d4fbcef37ec))
* **internal:** codegen related update ([3b9a132](https://github.com/meta-llama/llama-api-python/commit/3b9a132f8271d76851669aedab9ee880806a83e8))
* **internal:** detect missing future annotations with ruff ([b4cccf1](https://github.com/meta-llama/llama-api-python/commit/b4cccf14ca10e965177a0904692646da0c2892f0))
* **internal:** grammar fix (it's -&gt; its) ([46f738d](https://github.com/meta-llama/llama-api-python/commit/46f738d2b1bf8c210607abe2d1acc46f8361895d))
* **package:** drop Python 3.8 support ([785c446](https://github.com/meta-llama/llama-api-python/commit/785c4468206841d6c9d172b2733b0bcf053dcce6))
* speedup initial import ([cc25ae3](https://github.com/meta-llama/llama-api-python/commit/cc25ae390cb3e10aa517638ca25ba60b9e6b8b07))
* update lockfile ([2b01e25](https://github.com/meta-llama/llama-api-python/commit/2b01e25f540a589b7bedef48a3f18e0d4bba8d7d))

## 0.5.0 (2025-10-01)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/meta-llama/llama-api-python/compare/v0.4.0...v0.5.0)

### Features

* **api:** manual updates ([73a8579](https://github.com/meta-llama/llama-api-python/commit/73a85795b197c6ed820c18b88f8eac028e92ea20))
* file upload readme ([061b2cb](https://github.com/meta-llama/llama-api-python/commit/061b2cb1f03cc56c46f4f84d3b2feda1c54b0ed4))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([b0bf238](https://github.com/meta-llama/llama-api-python/commit/b0bf238b86c81b39a199b46e5ed03e6768d3e5ad))
* **types:** change optional parameter type from NotGiven to Omit ([19b3fdb](https://github.com/meta-llama/llama-api-python/commit/19b3fdbf3e0aa7d72e52b9b99f831fe2de0fbb04))

## 0.4.0 (2025-09-16)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/meta-llama/llama-api-python/compare/v0.3.0...v0.4.0)

### Features

* improve future compat with pydantic v3 ([648fe7b](https://github.com/meta-llama/llama-api-python/commit/648fe7be582adb6c50f73d24b32f6c9abdf88d73))
* **types:** replace List[str] with SequenceNotStr in params ([565a26d](https://github.com/meta-llama/llama-api-python/commit/565a26da9736a27ec88e1139e70569e3ba084b3a))


### Bug Fixes

* avoid newer type syntax ([b9bfeb3](https://github.com/meta-llama/llama-api-python/commit/b9bfeb3df2528b0c77017e9b1b50bcd54bf731bb))


### Chores

* **internal:** add Sequence related utils ([909f85f](https://github.com/meta-llama/llama-api-python/commit/909f85f12cb61ee164764bca656c0b574b0bcd2a))
* **internal:** move mypy configurations to `pyproject.toml` file ([68106c6](https://github.com/meta-llama/llama-api-python/commit/68106c6af940f1cbbbafae6dc0de999e1f853325))
* **internal:** update pydantic dependency ([9ad2fea](https://github.com/meta-llama/llama-api-python/commit/9ad2fea856c3470b20b89ddd033614eee40c0ea0))
* **internal:** update pyright exclude list ([203a1a1](https://github.com/meta-llama/llama-api-python/commit/203a1a1d8a74ece63939e25ec0a1b91c42706119))
* **tests:** simplify `get_platform` test ([21f3cd5](https://github.com/meta-llama/llama-api-python/commit/21f3cd5b775c2963be3d13ccfc59273c163fdfbc))

## 0.3.0 (2025-08-26)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/meta-llama/llama-api-python/compare/v0.2.0...v0.3.0)

### Features

* custom patch to handle exception during stream chunk ([7549f0b](https://github.com/meta-llama/llama-api-python/commit/7549f0b38d85143f984191bf9ff1f353f787fa50))


### Chores

* **internal:** change ci workflow machines ([37dd39f](https://github.com/meta-llama/llama-api-python/commit/37dd39fe156f7ed0f36101d014a4983498a10a27))
* **internal:** codegen related update ([cae389f](https://github.com/meta-llama/llama-api-python/commit/cae389f98552280557b2f73d0b146e159764a5a9))
* **internal:** update comment in script ([20ab448](https://github.com/meta-llama/llama-api-python/commit/20ab4484b71a0e9c555d28de0b8fbd59246851ac))
* run lint ([dc7d5a7](https://github.com/meta-llama/llama-api-python/commit/dc7d5a768eccf8c9d6faaac3585e7e09a611db02))
* update @stainless-api/prism-cli to v5.15.0 ([8e77df5](https://github.com/meta-llama/llama-api-python/commit/8e77df5e5778b55bda86a38735fb1426ae3a02a4))
* update github action ([3dab72d](https://github.com/meta-llama/llama-api-python/commit/3dab72dc5b6fc8ad8f9b9d72f25e155a7e22a857))

## 0.2.0 (2025-08-07)

Full Changelog: [v0.1.2...v0.2.0](https://github.com/meta-llama/llama-api-python/compare/v0.1.2...v0.2.0)

### Features

* clean up environment call outs ([4afbd01](https://github.com/meta-llama/llama-api-python/commit/4afbd01ed735b93d8b4c8c282881f2b78673995c))
* **client:** support file upload requests ([ec42e80](https://github.com/meta-llama/llama-api-python/commit/ec42e80b6249b3af1f3474ad4fba61d669ec0035))


### Bug Fixes

* **api:** remove chat completion request model ([94c4e9f](https://github.com/meta-llama/llama-api-python/commit/94c4e9fd500502781a0f6e30715ecbd134d015db))
* **client:** don't send Content-Type header on GET requests ([efec88a](https://github.com/meta-llama/llama-api-python/commit/efec88aa519948ea58ee629507cd91e9af90c1c8))
* **parsing:** correctly handle nested discriminated unions ([b627686](https://github.com/meta-llama/llama-api-python/commit/b6276863bea64a7127cdb71b6fbb02534d2e762b))
* **parsing:** ignore empty metadata ([d6ee851](https://github.com/meta-llama/llama-api-python/commit/d6ee85101e3e69c2768761e1187b8d33ee4e3762))
* **parsing:** parse extra field types ([f03ca22](https://github.com/meta-llama/llama-api-python/commit/f03ca2286018699dd29b964e9cbc1a66699ef59e))


### Chores

* add examples ([abfa065](https://github.com/meta-llama/llama-api-python/commit/abfa06572191caeaa33603c846d5953aa453521e))
* **internal:** bump pinned h11 dep ([d40e1b1](https://github.com/meta-llama/llama-api-python/commit/d40e1b1d736ec5e5fe7e3c65ace9c5d65d038081))
* **internal:** fix ruff target version ([c900ebc](https://github.com/meta-llama/llama-api-python/commit/c900ebc528a5f21e76f4742556577bbf33060f1c))
* **package:** mark python 3.13 as supported ([ef5bc36](https://github.com/meta-llama/llama-api-python/commit/ef5bc36693fa419e3d865e97cae97e7f5df19b1a))
* **project:** add settings file for vscode ([e310380](https://github.com/meta-llama/llama-api-python/commit/e3103801d608df4cff07da4e3eaae72df1391626))
* **readme:** fix version rendering on pypi ([786f9fb](https://github.com/meta-llama/llama-api-python/commit/786f9fbdb75e54ceac9eaf00d4c4d7002ed97a94))
* sync repo ([7e697f6](https://github.com/meta-llama/llama-api-python/commit/7e697f6550485728ee00d4fd18800a90fb3592ab))
* update SDK settings ([de22c0e](https://github.com/meta-llama/llama-api-python/commit/de22c0ece778c938f75e4717baf3e628c7a45087))


### Documentation

* code of conduct ([efe1af2](https://github.com/meta-llama/llama-api-python/commit/efe1af28fb893fa657394504dc8c513b20ac589a))
* readme and license ([d53eafd](https://github.com/meta-llama/llama-api-python/commit/d53eafd104749e9483015676fba150091e754928))
