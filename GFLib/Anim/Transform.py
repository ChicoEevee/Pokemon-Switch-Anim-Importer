# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Anim

import flatbuffers
from flatbuffers.compat import import_numpy

from GFLib.Anim.Vec3 import Vec3, Vec3T
from GFLib.Anim.Vec4 import Vec4, Vec4T

np = import_numpy()

class Transform(object):
    __slots__ = ['_tab']

    @classmethod
    def SizeOf(cls):
        return 40

    # Transform
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Transform
    def Scale(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 0)
        return obj

    # Transform
    def Rotate(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 12)
        return obj

    # Transform
    def Translate(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 28)
        return obj


def CreateTransform(builder, scale_x, scale_y, scale_z, rotate_x, rotate_y, rotate_z, rotate_w, translate_x, translate_y, translate_z):
    builder.Prep(4, 40)
    builder.Prep(4, 12)
    builder.PrependFloat32(translate_z)
    builder.PrependFloat32(translate_y)
    builder.PrependFloat32(translate_x)
    builder.Prep(4, 16)
    builder.PrependFloat32(rotate_w)
    builder.PrependFloat32(rotate_z)
    builder.PrependFloat32(rotate_y)
    builder.PrependFloat32(rotate_x)
    builder.Prep(4, 12)
    builder.PrependFloat32(scale_z)
    builder.PrependFloat32(scale_y)
    builder.PrependFloat32(scale_x)
    return builder.Offset()

try:
    from typing import Optional
except:
    pass

class TransformT(object):

    # TransformT
    def __init__(self):
        self.scale = None  # type: Optional[Vec3T]
        self.rotate = None  # type: Optional[Vec4T]
        self.translate = None  # type: Optional[Vec3T]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        transform = Transform()
        transform.Init(buf, pos)
        return cls.InitFromObj(transform)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, transform):
        x = TransformT()
        x._UnPack(transform)
        return x

    # TransformT
    def _UnPack(self, transform):
        if transform is None:
            return
        if transform.Scale(Vec3()) is not None:
            self.scale = Vec3T.InitFromObj(transform.Scale(Vec3()))
        if transform.Rotate(Vec4()) is not None:
            self.rotate = Vec4T.InitFromObj(transform.Rotate(Vec4()))
        if transform.Translate(Vec3()) is not None:
            self.translate = Vec3T.InitFromObj(transform.Translate(Vec3()))

    # TransformT
    def Pack(self, builder):
        return CreateTransform(builder, self.scale.x, self.scale.y, self.scale.z, self.rotate.x, self.rotate.y, self.rotate.z, self.rotate.w, self.translate.x, self.translate.y, self.translate.z)