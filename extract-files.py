#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/oplus',
    'hardware/qcom-caf/sm8450',
    'vendor/oneplus/sm8450-common',
    'vendor/qcom/opensource/commonsys-intf/display',
]


def lib_fixup_odm_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}'


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    ('vendor.qti.hardware.pal@1.0-impl',): lib_fixup_odm_suffix,
    (): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    'odm/bin/hw/vendor.oplus.hardware.cammidasservice-V1-service': blob_fixup()
        .replace_needed('android.frameworks.stats-V1-ndk_platform.so', 'android.frameworks.stats-V1-ndk.so'),
    'odm/vendor/etc/wifi/WCNSS_qcom_cfg.ini': blob_fixup()
        .regex_replace('BandCapability=3', ''),
    'odm/lib64/libAlgoProcess.so': blob_fixup()
        .replace_needed('android.hardware.graphics.common-V2-ndk_platform.so', 'android.hardware.graphics.common-V6-ndk.so')
        .replace_needed('vendor.oplus.hardware.osense.client-V1-ndk_platform.so', 'vendor.oplus.hardware.osense.client-V1-ndk.so'),
    ('odm/lib64/libaps_frame_registration.so', 'odm/lib64/libCOppLceTonemapAPI.so', 'odm/lib64/libCS.so', 'odm/lib64/libSuperRaw.so', 'odm/lib64/libYTCommon.so', 'odm/lib64/libyuv2.so'): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'odm/bin/hw/vendor.oplus.hardware.biometrics.fingerprint@2.1-service_uff': blob_fixup()
        .replace_needed('android.hardware.biometrics.fingerprint-V1-ndk_platform.so', 'android.hardware.biometrics.fingerprint-V2-ndk.so')
        .replace_needed('android.hardware.biometrics.common-V1-ndk_platform.so', 'android.hardware.biometrics.common-V2-ndk.so')
        .replace_needed('vendor.oplus.hardware.commondcs-V1-ndk_platform.so', 'vendor.oplus.hardware.commondcs-V1-ndk.so')
        .replace_needed('vendor.oplus.hardware.touch-V1-ndk_platform.so', 'vendor.oplus.hardware.touch-V1-ndk.so')
        .replace_needed('vendor.oplus.hardware.osense.client-V1-ndk_platform.so', 'vendor.oplus.hardware.osense.client-V1-ndk.so')
        .add_needed('libshims_aidl_fingerprint_v2.oplus.so'),
    'odm/lib64/libolc_vnd.so': blob_fixup()
        .replace_needed('vendor.oplus.hardware.touch-V1-ndk_platform.so', 'vendor.oplus.hardware.touch-V1-ndk.so')
        .replace_needed('vendor.oplus.hardware.olc2-V1-ndk_platform.so', 'vendor.oplus.hardware.olc2-V2-ndk.so'),
    ('odm/lib64/camera/com.qti.sensor.ovaltine_imx766.so',
            'odm/lib64/camera/com.qti.sensor.ovaltine_ov02b.so',
            'odm/lib64/camera/com.qti.sensor.ovaltine_ov08d.so',
            'odm/lib64/camera/com.qti.sensor.ovaltine_s5k3p9.so',
            'odm/lib64/libosenseaidlhalclient.so',
            'odm/lib64/vendor.oplus.hardware.cameraextension-V1-service-impl.so',
            'odm/lib64/vendor.oplus.hardware.sendextcamcmd-V1-service-impl.so',
            'vendor/lib64/camera/components/com.arcsoft.node.eisv2.so',
            'vendor/lib64/camera/components/com.bots.node.vendortagwrite.so',
            'vendor/lib64/camera/components/com.qti.camx.chiiqutils.so',
            'vendor/lib64/camera/components/com.qti.node.depth.so',
            'vendor/lib64/camera/components/com.qti.node.dewarp.so',
            'vendor/lib64/camera/components/com.qti.node.eisv2.so',
            'vendor/lib64/camera/components/com.qti.node.eisv3.so',
            'vendor/lib64/camera/components/com.qti.node.gme.so',
            'vendor/lib64/camera/components/com.qti.node.gyrornn.so',
            'vendor/lib64/camera/components/com.qti.node.hdr10pgen.so',
            'vendor/lib64/camera/components/com.qti.node.hdr10phist.so',
            'vendor/lib64/camera/components/com.qti.node.ml.so',
            'vendor/lib64/camera/components/com.qti.node.mlinference.so',
            'vendor/lib64/camera/components/com.qti.node.swec.so',
            'vendor/lib64/camera/components/com.qti.node.swregistration.so',
            'vendor/lib64/camera/components/libdepthmapwrapper_secure.so',
            'vendor/lib64/com.qti.chiusecaseselector.so',
            'vendor/lib64/com.qti.feature2.anchorsync.so',
            'vendor/lib64/com.qti.feature2.demux.so',
            'vendor/lib64/com.qti.feature2.derivedoffline.so',
            'vendor/lib64/com.qti.feature2.frameselect.so',
            'vendor/lib64/com.qti.feature2.fusion.so',
            'vendor/lib64/com.qti.feature2.generic.so',
            'vendor/lib64/com.qti.feature2.gs.cedros.so',
            'vendor/lib64/com.qti.feature2.gs.fillmore.so',
            'vendor/lib64/com.qti.feature2.gs.sdm865.so',
            'vendor/lib64/com.qti.feature2.gs.sm8350.so',
            'vendor/lib64/com.qti.feature2.gs.sm8450.so',
            'vendor/lib64/com.qti.feature2.hdr.so',
            'vendor/lib64/com.qti.feature2.mcreprocrt.so',
            'vendor/lib64/com.qti.feature2.memcpy.so',
            'vendor/lib64/com.qti.feature2.mfsr.fillmore.so',
            'vendor/lib64/com.qti.feature2.mfsr.netrani.so',
            'vendor/lib64/com.qti.feature2.mfsr.sm8450.so',
            'vendor/lib64/com.qti.feature2.mfsr.so',
            'vendor/lib64/com.qti.feature2.ml.fillmore.so',
            'vendor/lib64/com.qti.feature2.ml.so',
            'vendor/lib64/com.qti.feature2.mux.so',
            'vendor/lib64/com.qti.feature2.qcfa.so',
            'vendor/lib64/com.qti.feature2.rawhdr.so',
            'vendor/lib64/com.qti.feature2.realtimeserializer.so',
            'vendor/lib64/com.qti.feature2.rt.so',
            'vendor/lib64/com.qti.feature2.rtmcx.so',
            'vendor/lib64/com.qti.feature2.serializer.so',
            'vendor/lib64/com.qti.feature2.statsregeneration.so',
            'vendor/lib64/com.qti.feature2.stub.so',
            'vendor/lib64/com.qti.feature2.swmf.so',
            'vendor/lib64/com.qti.qseeutils.so',
            'vendor/lib64/com.qualcomm.mcx.distortionmapper.so',
            'vendor/lib64/com.qualcomm.mcx.linearmapper.so',
            'vendor/lib64/com.qualcomm.mcx.policy.mfl.so',
            'vendor/lib64/com.qualcomm.mcx.policy.xr.so',
            'vendor/lib64/com.qualcomm.qti.mcx.usecase.extension.so',
            'vendor/lib64/hw/camera.qcom.so',
            'vendor/lib64/hw/com.qti.chi.override.so',
            'vendor/lib64/libcamerapostproc.so',
            'vendor/lib64/libcamxcommonutils.so',
            'vendor/lib64/vendor.qti.hardware.camera.aon@1.0-service-impl.so',
            'vendor/lib64/vendor.qti.hardware.camera.postproc@1.0-service-impl.so'): blob_fixup()
        .replace_needed('vendor.oplus.hardware.commondcs-V1-ndk_platform.so', 'vendor.oplus.hardware.commondcs-V1-ndk.so')
        .replace_needed('vendor.oplus.hardware.osense.client-V1-ndk_platform.so', 'vendor.oplus.hardware.osense.client-V1-ndk.so')
        .replace_needed('vendor.oplus.hardware.performance-V1-ndk_platform.so', 'vendor.oplus.hardware.performance-V1-ndk.so'),
    'odm/etc/camera/CameraHWConfiguration.config': blob_fixup()
        .regex_replace('SystemCamera = 0;  0;  0;  1;  0;  1;', 'SystemCamera = 0;  0;  0;  0;  0;  0;'),
    'odm/lib64/libarcsoft_high_dynamic_range_v4.so': blob_fixup()
        .clear_symbol_version('remote_handle_close')
        .clear_symbol_version('remote_handle_invoke')
        .clear_symbol_version('remote_handle_open')
        .clear_symbol_version('remote_register_buf_attr')
        .clear_symbol_version('remote_register_buf'),
    'odm/lib64/libextensionlayer.so': blob_fixup()
        .replace_needed('libziparchive.so', 'libziparchive_odm.so')
        .replace_needed('vendor.oplus.hardware.osense.client-V1-ndk_platform.so', 'vendor.oplus.hardware.osense.client-V1-ndk.so')
        .replace_needed('vendor.oplus.hardware.performance-V1-ndk_platform.so', 'vendor.oplus.hardware.performance-V1-ndk.so'),
    'product/etc/sysconfig/com.android.hotwordenrollment.common.util.xml': blob_fixup()
        .regex_replace('/my_product', '/product'),
    'vendor/lib64/libcamximageformatutils.so': blob_fixup()
        .replace_needed('vendor.oplus.hardware.commondcs-V1-ndk_platform.so', 'vendor.oplus.hardware.commondcs-V1-ndk.so')
        .replace_needed('vendor.oplus.hardware.performance-V1-ndk_platform.so', 'vendor.oplus.hardware.performance-V1-ndk.so')
        .replace_needed('vendor.oplus.hardware.osense.client-V1-ndk_platform.so', 'vendor.oplus.hardware.osense.client-V1-ndk.so')
        .replace_needed('vendor.qti.hardware.display.config-V2-ndk_platform.so', 'vendor.qti.hardware.display.config-V2-ndk.so'),
    ('odm/lib64/libOGLManager.so'): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    'vendor/lib64/sensors.ssc.so': blob_fixup()
        .binary_regex_replace(b'qti.sensor.wise_light', b'android.sensor.light\x00')
        .sig_replace('EA D3 84 52 01 41 00 91 29 00 17 CB 29 41 00 D1 29 15 C9 93 4A 3F A0 72', 'AA 00 80 52 01 41 00 91 29 00 17 CB 29 41 00 D1 29 15 C9 93 0A 00 A0 72'),
}  # fmt: skip

module = ExtractUtilsModule(
    'ovaltine',
    'oneplus',
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    add_firmware_proprietary_file=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8450-common', module.vendor
    )
    utils.run()
