#
# Copyright (C) 2021-2023 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Include the common OEM chipset BoardConfig.
include device/oneplus/sm8450-common/BoardConfigCommon.mk

DEVICE_PATH := device/oneplus/ovaltine

# Kernel
TARGET_KERNEL_CONFIG += vendor/oplus/ovaltine.config

# Partitions
ifeq (,$(filter true, $(WITHOUT_RESERVED_SIZE) $(WITH_GMS)))
BOARD_PRODUCTIMAGE_PARTITION_RESERVED_SIZE := 900000000
endif
BOARD_ONEPLUS_DYNAMIC_PARTITIONS_SIZE := 5637144572
BOARD_SUPER_PARTITION_SIZE := 11274289152

# Properties
TARGET_VENDOR_PROP += $(DEVICE_PATH)/vendor.prop

# Recovery
TARGET_RECOVERY_UI_MARGIN_HEIGHT := 103

# Include the proprietary files BoardConfig.
include vendor/oneplus/ovaltine/BoardConfigVendor.mk
