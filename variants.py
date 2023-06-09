'''
Copyright 2023 Sam A. Haygood

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

from tile import Tile
from piece import Piece
import pickle
import copy
from render_engines import GraphRenderEngine

class Variants:
    def save(name, render_engine, file_path = 'presets'):
        path = f"saved/{file_path}/{name}.ucbgame"
        try:
            with open(path, 'xb') as f:
                pickle.dump(render_engine, f)
        except:
            with open(path, 'wb') as f:
                pickle.dump(render_engine, f)
        print(f'{name} Preset Saved')

    def load(name, file_path = 'presets') -> GraphRenderEngine:
        path = f"saved/{file_path}/{name}.ucbgame"
        with open(path, 'rb') as f:
            preset = pickle.load(f)
        print(f'{name} Preset Loaded')
        return preset

